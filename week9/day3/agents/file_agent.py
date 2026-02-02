from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from day3.tools.file_tool import FILE_TOOLS
import os
from dotenv import load_dotenv

load_dotenv()

model_client = OpenAIChatCompletionClient(
    model="openai/gpt-oss-20b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("api_key"),
    model_info={
        "family": "llama",
        "context_length": 8192,
        "function_calling": True,
        "vision": True,
        "json_output": False,
        "structured_output":True
    },
    parallel_tool_calls=False
)
FileAgent = AssistantAgent(
    name="FileAgent",
    model_client=model_client,
    system_message="""
You are a File Agent.
You MUST follow the plan provided by orchestrator strictly.
You can read and write .txt and .csv files using tools.
You NEVER write code
You NEVER query database
(Database path to load the csv : "sales.db")
RESPONSIBILITIES:
- Inspect CSV structure (columns, row count)
- Read and write .txt files
- You can read some number of columns from the csv using the read_csv_tool to have a look at data.
- If the task involves Quering the CSV file , you must put the csv file in database with the help of tools and DB agent will handle from there.
""",
    tools=FILE_TOOLS
)