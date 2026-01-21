from day1.protocol.message_protocol import MessageProtocol
from day1.memory.session_memory import Memory


class ResearchAgent:
    def __init__(self,llm):
        self.name = "research_agent"
        self.system_prompt = (
            """
            You are a Research Agent.
            Your job is ONLY to gather factual information related to the user's query.
            Return factual bullet-point research

            Rules:
            - Do NOT summarize.
            - Do NOT answer the user directly.
            - Do NOT add opinions.
            - Return raw researched information only.
            """
        )
        self.llm = llm
        self.memory = Memory(window_size=10)

    def handle(self, user_message):
        self.memory.add(user_message)
        user_prompt = f"""
        Researchable content:
        {user_message["content"]}

        Do a research.
        """
    
        raw_response = self.llm.generate(self.system_prompt, user_prompt)

        message = MessageProtocol.create(
            sender=self.name,
            receiver="summarizer_agent",
            role="assistant",
            content=raw_response
        )

        self.memory.add(message)
        return message
