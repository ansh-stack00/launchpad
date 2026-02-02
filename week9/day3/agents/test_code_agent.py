from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from day3.tools.code_executor import code_tool
import os
from dotenv import load_dotenv

load_dotenv()
model_client = OpenAIChatCompletionClient(
    model="openai/gpt-oss-20b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("api_key"),
    model_info={
        "family": "openai",
        "context_length": 8192,
        "function_calling": True,
        "vision": True,
        "json_output": False,
        "structured_output":True
    },
    parallel_tool_calls=False
)

CodeAgent = AssistantAgent(
    name="CodeAgent",
    model_client=model_client,
    system_message="""
You are a Python Code Execution Agent.

RULES:
- You CAN write new logic but ONLY if specefied EXPLICITLY. Otherwise You ONLY execute code exactly as provided.
- You execute the Python code provided by the user.
- You MUST always use the tool for code execution.
- You MUST return the real execution output.
- If execution fails, return the full error traceback.
""",
    tools=[code_tool],
)