from core.gemini_client import initialize_gemini
from agents.summarizer import SummarizerAgent
from agents.qa_agent import QAAgent
from agents.code_explainer import CodeExplainerAgent

def main():
    model = initialize_gemini()

    agents = {
        "1": ("Summarize Text", SummarizerAgent(model)),
        "2": ("Question Answering", QAAgent(model)),
        "3": ("Explain Code", CodeExplainerAgent(model))
    }

    print("🔮 GenAI Agentic Assistant 🔮")
    print("Choose an agent:")
    for key, (desc, _) in agents.items():
        print(f"{key}. {desc}")

    choice = input("Enter choice: ").strip()
    if choice not in agents:
        print("Invalid choice.")
        return

    prompt = input("Enter your input: ")
    agent = agents[choice][1]
    output = agent.run(prompt)

    print("\n🧠 Output:")
    print(output)

if __name__ == "__main__":
    main()
