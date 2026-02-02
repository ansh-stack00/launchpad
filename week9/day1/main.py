from day1.agent.research_agent import ResearchAgent
from day1.agent.summarizer_agent import SummarizerAgent
from day1.agent.answer_agent import AnswerAgent
from day1.agent.base_agent import LocalLLM


class AgentOrchestrator:
    """
    Flow:
    User -> Research -> Summarizer -> Answer -> User
    """

    def __init__(self):
        llm = LocalLLM()
        self.research_agent = ResearchAgent(llm)
        self.summarizer_agent = SummarizerAgent(llm)
        self.answer_agent = AnswerAgent(llm)

    def run(self, user_query: str) -> str:
    
        research_msg = self.research_agent.process(user_query)
        print("RESEARCH RESULTS:\n" + research_msg.content + "\n")
        summary_msg = self.summarizer_agent.process(
            research_msg.content
        )
        print("SUMMARY:\n" + summary_msg.content + "\n")
        answer_msg = self.answer_agent.process(
            summary_msg.content
        )
        return answer_msg.content


if __name__ == "__main__":
    orch = AgentOrchestrator()

    query = input("Ask: ")
    result = orch.run(query)

    print("\nFINAL ANSWER:\n")
    print(result)