from autogen_agentchat.agents import AssistantAgent
from day3.tools.file_tool import (read_txt_tool, write_txt_tool, append_txt_tool,
    read_csv_tool, write_csv_tool)
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
from dotenv import load_dotenv
import os 

load_dotenv()
BASE_DIR = os.getcwd()

model_client = OpenAIChatCompletionClient(
    model="llama-3.3-70b-versatile", 
    base_url="https://api.groq.com/openai/v1",  
    api_key=os.getenv('api_key'),
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "family": "llama-3.3",
        "structured_output": True,
    }    
)

code_agent = AssistantAgent(
    name="FileAgent",
    model_client=model_client,
    system_message="""You are a File Agent. You can read/write .txt and .csv files using tools.
        Use read tools to inspect files, and write tools to save outputs.""",
    tools=[read_txt_tool, write_txt_tool, append_txt_tool,
    read_csv_tool, write_csv_tool]
)

task = f"""
Analyze the csv and generate 5 insights 
CSV file at path: {BASE_DIR}/sales_data_sample.csv
"""
async def main():
    response = await code_agent.run(task=task)
    print(response.messages[-1].content)


asyncio.run(main())
