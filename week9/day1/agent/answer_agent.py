from day1.protocol.message_protocol import MessageProtocol
from day1.memory.session_memory import Memory

class AnswerAgent:
    def __init__(self,llm):
        self.name = "answer_agent"
        self.system_prompt = (
            """
                You are an Answer Agent.
                Explain the provided summary into a helpful, natural answer.
                Rules:
                - Do NOT re-research.
                - Do NOT invent facts.
                - Do NOT mention internal agents.
            """
        )
        self.llm = llm
        self.memory = Memory(window_size=10)


    def handle(self, summary_message, user_message):
        self.memory.add(summary_message)
        self.memory.add(user_message)
        user_prompt = f"""
        summarized content:
        {summary_message["content"]}

         Answer using the summarized content.
        """

        raw_response = self.llm.generate(self.system_prompt , user_prompt)

        message = MessageProtocol.create(
            sender=self.name,
            receiver="user",
            role="assistant",
            content=raw_response
        )

        self.memory.add(message)
        return message