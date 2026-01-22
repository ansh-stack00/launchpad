from orchestrator.planner import create_planner_agent,plan_tasks 
from agents.worker_agent import run_workers_parallel
from agents.reflactor_agent  import create_reflection_agent, reflect_answer
from agents.validator_agent import create_validator_agent, validate_answer
from utils.dag import init_task_status, get_ready_tasks, print_dag_state
from utils.models import TaskStatus
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio


model_client = OpenAIChatCompletionClient(
        model="llama-3.3-70b-versatile", 
        base_url="https://api.groq.com/openai/v1",
        api_key="",  
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "family": "llama-3.3",
            "structured_output": True,
        }    
)



async def main():
    query = "explain the tarrif sheme of U.S which was implemented in 2025"

    planner_agent = create_planner_agent(model_client)
    reflection_agent = create_reflection_agent(model_client)
    validator_agent = create_validator_agent(model_client)

    # Step 1: Planning
    plan = await plan_tasks(planner_agent, query)

    # Step 2: Init DAG
    task_status = init_task_status(plan)
    task_results = {}

    print_dag_state("INITIAL", plan, task_status)

    # Step 3: DAG Execution
    while len(task_results) < len(plan.tasks):

        ready_tasks = get_ready_tasks(plan, task_status)

        if not ready_tasks:
            raise RuntimeError("Deadlock detected in DAG. Check dependencies.")

        for t in ready_tasks:
            task_status[t.id] = TaskStatus.RUNNING

        print_dag_state("RUNNING", plan, task_status)

        results = await run_workers_parallel(ready_tasks, model_client)

        for task_id, output in results.items():
            task_status[task_id] = TaskStatus.DONE
            task_results[task_id] = output

        print_dag_state("DONE", plan, task_status)

    # Step 4: Merge outputs
    merged_output = "\n\n".join(
        task_results[t.id] for t in plan.tasks
    )

    # Step 5: Reflection
    print("\n--- REFLECTION STAGE ---")
    improved = await reflect_answer(reflection_agent, merged_output)

    # Step 6: Validation
    print("\n--- VALIDATION STAGE ---")
    verdict = await validate_answer(validator_agent, improved)

    print("\n--- FINAL ANSWER ---")
    print(improved)

    print("\n--- VALIDATION RESULT ---")
    print(f"Verdict: {verdict.verdict}")
    print(f"Reason: {verdict.reason}")


if __name__ == "__main__":
   asyncio.run(main())
