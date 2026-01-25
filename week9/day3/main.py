import os
import asyncio
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from day3.agents.code_gen_agent import CodeGen_agent
from day3.agents.test_code_agent import code_agent
from day3.agents.file_agent import  file_agent
from day3.agents.DB_agent import Db_agent
from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
load_dotenv()

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

async def call_codegen_agent(task: str) -> str:
    result = await CodeGen_agent.run(task=task)
    return result.messages[-1].content

codegen_tool = FunctionTool(
    call_codegen_agent,
    "Generate Python code based on a task."
)

async def call_codeexec_agent(task: str) -> str:
    result = await code_agent.run(task=task)
    return result.messages[-1].content

codeexec_tool = FunctionTool(
    call_codeexec_agent,
    "Execute Python code and return output."
)

async def call_file_agent(task: str) -> str:
    result = await file_agent.run(task=task)
    return result.messages[-1].content

file_tool = FunctionTool(
    call_file_agent,
    "Call File Agent to read or write files. Provide task like 'Save this code to analysis.py'."
)
async def call_db_agent(task: str) -> str:
    result = await Db_agent.run(task=task)
    return result.messages[-1].content

db_tool = FunctionTool(
    call_db_agent,
    "Use DB Agent to inspect schema or run SQL queries."
)



SYSTEM_PROMPT = """
You are a General Orchestrator Agent.

You NEVER perform the task yourself.

You have access to these helper agents:
- File Agent: for reading/writing txt and csv files
- CodeGen Agent: for generating Python code
- CodeExec Agent: for executing Python code
- DB Agent: for answering database questions

CRITICAL RULES:
- NEVER write SQL yourself.
- NEVER write Python code yourself.
- ALWAYS pass the user's request in NATURAL LANGUAGE to the appropriate agent.
- The DB Agent is the ONLY agent allowed to generate SQL.
- If the user asks about database data, forward the request AS-IS to the DB Agent.
- If the user asks to generate and run code → always call CodeGenAgent then CodeExecAgent
- Never assume outputs; always get them from the actual agent
- Always use natural language when routing tasks to agents

Your job:
1. Understand the user intent
2. Decide which agent(s) can handle it
3. Call them with a clear natural-language task
4. Return the final answer

Do not transform the task into SQL or code.

### FEW-SHOT EXAMPLES

#### User:
Generate Python code that reads sales_data_sample.csv, computes top 5 products by revenue, and print the result

#### Orchestrator Plan:
1. Call CodeGenAgent with the user task and get the generated code 
2. Call CodeExecutorAgent with: "Please execute this code:\n[generated_code]"
4. Return both the code and the printed output

---

#### User:
Summarize the content of report.txt and save it in summary.txt

#### Orchestrator Plan:
1. Call FileAgent to read report.txt
2. Send the content to CodeGenAgent with prompt: "Summarize this text into 3 bullet points:\n[data]"
3. Call CodeExecutorAgent with the generated summarizer code
4. Call FileAgent to save output into summary.txt

User:
Generate Python code and execute it to analyze sales_data.csv

Orchestrator Plan:
1. Call CodeGenAgent with user task
2. Get code
3. Call CodeExecAgent with that code
4. Return both code and output

IMPORTANT:
- You may need to call multiple tools in sequence
- Always continue execution until the full user request is fulfilled
- When calling the CodeExec agent, pass the full code string directly in the `code` field.
- Do NOT pass variable names like `generated_code`. They are not defined.
- For example, use: {"code": "print('Hello world')"} NOT {"code": "generated_code"}

"""



orchestrator_agent = AssistantAgent(
    name="orchestrator",
    model_client=model_client,
    system_message=SYSTEM_PROMPT,
    tools=[file_tool,codegen_tool,codeexec_tool,db_tool],

)

async def main():
    task = input("User Task: ")  
    result = await orchestrator_agent.run(task=task)

    final_message = result.messages[-1].content
# code execution fallback    
    if "```python" in final_message:
        code = final_message.split("```python")[1].split("```")[0].strip()

        print("\nCode Generated:\n", code)
        exec_result = await code_agent.run(
            task=f"Please execute this code:\n{code}"
        )

        print("\nCode Output:\n", exec_result.messages[-1].content)
    else:
        print("\nFinal Result:\n", final_message)

asyncio.run(main())