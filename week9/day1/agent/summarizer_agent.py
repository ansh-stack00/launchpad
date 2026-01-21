from day1.protocol.message_protocol import MessageProtocol
from day1.memory.session_memory import Memory

class SummarizerAgent:
    def __init__(self,llm):
        self.name = "summarizer_agent"
        self.system_prompt = ("""
                You are a Summarizer Agent."
                Your job is to preserve ALL key ideas while shortening the text.
                Do NOT collapse concepts into single words.
                Compress research into a concise summary.
                Do not add new information or facts .
            """
        )
        self.llm = llm
        self.memory = Memory(window_size=10)


    def handle(self, research_message):

        user_prompt = f"""
        research content:
        {research_message["content"]}

        Summarize the research.
        """
        self.memory.add(research_message)

        raw_response = self.llm.generate(self.system_prompt , user_prompt)

        message = MessageProtocol.create(
            sender=self.name,
            receiver="answer_agent",
            role="assistant",
            content=raw_response
        )

        self.memory.add(message)
        return message