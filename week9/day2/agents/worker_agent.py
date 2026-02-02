from autogen_agentchat.agents import AssistantAgent


def create_worker_agent(name, model_client):
    """
    Worker Agent executes a single task.
    """
    return AssistantAgent(
        name=name,
        system_message="""
You are a Worker Agent.

Execute ONLY the assigned task.
Be precise and factual.
Return clear output.
""",
        model_client=model_client,
    )
