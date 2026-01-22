from typing import Dict
from utils.models import TaskStatus, PlanModel

def init_task_status(plan: PlanModel) -> Dict[str, TaskStatus]:
    return {t.id: TaskStatus.PENDING for t in plan.tasks}

def get_ready_tasks(plan: PlanModel, task_status: Dict[str, TaskStatus]):
    return [
        t for t in plan.tasks
        if task_status[t.id] == TaskStatus.PENDING
        and all(task_status[dep] == TaskStatus.DONE for dep in t.deps)
    ]


def print_dag_state(step_name: str, plan: PlanModel, task_status: Dict[str, TaskStatus]):
    print(f"\n--- DAG STATE: {step_name} ---")
    for t in plan.tasks:
        deps = ",".join(t.deps) if t.deps else "-"
        print(f"{t.id:<8} | deps: {deps:<15} | status: {task_status[t.id]}")
    print("-" * 50)
