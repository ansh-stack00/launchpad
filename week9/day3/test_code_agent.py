from autogen_agentchat.agents import AssistantAgent
from day3.tools.code_executor import code_tool
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
from dotenv import load_dotenv
import os 

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

code_agent = AssistantAgent(
    name="CodeAgent",
    model_client=model_client,
    system_message="You are a CodeAgent. Your job is to execute Python code sent to you and return the output.",
    tools=[code_tool]
)

async def main():
    response = await code_agent.run(task="""Please execute the following Python code:

```python
for i in range(3):
    print("Ansh")
```""")
    print(response.messages[-1].content)


asyncio.run(main())
