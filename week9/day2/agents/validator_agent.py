import json
import re
from autogen_agentchat.agents import AssistantAgent


def create_validator_agent(model_client):

    return AssistantAgent(
        name="validator",
        system_message="""
You are a Validator Agent.

Check:
- correctness
- completeness
- logic

Return ONLY JSON:

{
 "verdict": "PASS" or "FAIL",
 "reason": "short explanation"
}

NO markdown.
NO extra text.
""",
        model_client=model_client,
    )


def extract_json(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON found")
    return json.loads(match.group())
