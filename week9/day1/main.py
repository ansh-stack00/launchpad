from day1.protocol.message_protocol import MessageProtocol
from day1.agent.research_agent import ResearchAgent
from day1.agent.summarizer_agent import SummarizerAgent
from day1.agent.answer_agent import AnswerAgent
from day1.llm.llm_client import LocalLLM


def main():
    llm=LocalLLM()
    research_agent = ResearchAgent(llm)
    summarizer_agent = SummarizerAgent(llm)
    answer_agent = AnswerAgent(llm)

    print("=== Day 1: Message-Protocol Agent System ===\n")

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        user_message = MessageProtocol.create(
            sender="user",
            receiver="research_agent",
            role="user",
            content=user_input
        )

        research_message = research_agent.handle(user_message)
        print("\n[Research Agent]\n", research_message["content"])

        summary_message = summarizer_agent.handle(research_message)
        print("\n[Summarizer Agent]\n", summary_message["content"])

        answer_message = answer_agent.handle(summary_message, user_message)
        print("\n[Answer Agent]\n", answer_message["content"])


if __name__ == "__main__":
    main()
