from agents.planner import plan_task
from agents.researcher import run_research
from agents.summarizer import summarize_content
from agents.memory import save_to_memory

def main():
    print("🤖 Welcome to Intelligent Task Agent!")
    task = input("Enter your main research task: ")
    
    subtasks = plan_task(task)
    print("\n📌 Subtasks generated:")
    for s in subtasks:
        print(f"- {s}")

    results = []
    for sub in subtasks:
        research = run_research(sub)
        save_to_memory(research)
        results.append(research)

    summary = summarize_content(results)
    print("\n✅ Final Report:\n")
    print(summary)

if __name__ == "__main__":
    main()
