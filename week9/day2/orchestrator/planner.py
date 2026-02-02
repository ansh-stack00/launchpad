import asyncio
import json
import re
import networkx as nx
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from day2.agents.worker_agent import create_worker_agent
from day2.agents.validator_agent import create_validator_agent, extract_json
import os 
from dotenv import load_dotenv

load_dotenv()

model_client = OpenAIChatCompletionClient(
        model="llama-3.3-70b-versatile", 
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("api_key"),  
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "family": "llama-3.3",
            "structured_output": True,
        }    
)


def create_planner_agent():

    return AssistantAgent(
        name="planner",
        system_message="""
Break the user query into tasks.

Return JSON:

{
 "tasks":[
  {"id":"t1","task":"...","deps":[]},
  {"id":"t2","task":"...","deps":["t1"]}
 ]
}

Rules:
- Make tasks atomic
- Allow parallel tasks
- Include a final synthesis task
""",
        model_client=model_client,
    )


def create_reflection_agent():

    return AssistantAgent(
        name="reflection",
        system_message="""
Improve clarity and structure.
Fix weak phrasing.
Do NOT add new facts.
Return improved answer only.
""",
        model_client=model_client,
    )



def extract_json_block(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("Planner did not return JSON")
    return json.loads(match.group())


def get_execution_levels(G):
    return list(nx.topological_generations(G))


async def run(query: str):

    print("\n--- PLANNING ---")

    planner = create_planner_agent()
    plan_reply = await planner.run(task=query)

    plan = extract_json_block(plan_reply.messages[-1].content)
    tasks = plan["tasks"]

    # mappinf for easy lookup 
    task_map = {t["id"]: t for t in tasks}

    G = nx.DiGraph()
    for t in tasks:
        G.add_node(t["id"])
        for d in t["deps"]:
            G.add_edge(d, t["id"])

    levels = get_execution_levels(G)

    print("\nEXECUTION TREE (WITH TASKS):")

    for i, lvl in enumerate(levels):
        print(f"\nLevel {i}:")
        for task_id in lvl:
            print(f"  {task_id} → {task_map[task_id]['task']}")

  
    results = {}

    for i, level in enumerate(levels):

        print(f"\n--- RUNNING LEVEL {i} ---")

        coros = []
        task_ids = []

        for task_id in level:
            task_desc = task_map[task_id]["task"]

            print(f"\n-> Worker {task_id} executing:")
            print(f"   Task: {task_desc}")

            worker = create_worker_agent(task_id, model_client)

            coros.append(worker.run(task=task_desc))
            task_ids.append(task_id)

        outputs = await asyncio.gather(*coros)

        for task_id, out in zip(task_ids, outputs):
            result_text = out.messages[-1].content
            results[task_id] = result_text

            print(f"\nOutput from {task_id}:")
            print(result_text[:500], "...")


    merged = "\n".join(results.values())

    print("\n--- MERGED OUTPUT ---\n")
    print(merged[:1000], "...")
    print("\n--- REFLECTION ---")
    reflector = create_reflection_agent()
    ref_out = await reflector.run(task=merged)
    improved = ref_out.messages[-1].content

    print("\nREFLECTION OUTPUT:\n")
    print(improved)

  
    print("\n--- VALIDATION ---")

    validator = create_validator_agent(model_client)
    val_out = await validator.run(task=improved)
    verdict = extract_json(val_out.messages[-1].content)
    print("\nVALIDATION RESULT:")
    print(verdict)

    print("FINAL ANSWER")
    print(improved)

if __name__ == "__main__":
    query = input("Enter query: ")
    asyncio.run(run(query))
