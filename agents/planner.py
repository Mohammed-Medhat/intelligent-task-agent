from utils.gemini import gemini_chat
import re

def plan_task(task):
    prompt = f"""Break down this task into 4 subtasks suitable for a research agent.

Task: {task}

Only return each subtask on a new line without any markdown (*, -, etc.).
"""
    response = gemini_chat(prompt)

    # Clean up each line, remove extra formatting
    lines = response.split("\n")
    subtasks = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Remove leading symbols like *, -, or numbering
        line = re.sub(r"^[-*•\d\.\s]+", "", line)
        subtasks.append(line)
    return subtasks
