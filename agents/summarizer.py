from utils.gemini import gemini_chat

def summarize_content(results, size="Medium"):
    content = "\n\n".join([f"{r['subtask']}:\n{r['content']}" for r in results])

    instructions = {
        "Small": "Write a brief executive summary in 3–5 sentences (max ~600 tokens). Focus only on the high-level takeaways.",
        "Medium": "Summarize the key findings with brief comparisons and some insights (around 800–1000 tokens) add summary.",
        "Large": "Write a full detailed report including comparisons, pros and cons, and final recommendations (up to 2000 tokens) add summary."
    }

    prompt = f"""
You are an expert technical analyst tasked with helping users understand results from multiple AI agents assigned to a research task.

Your goal is to produce a structured and insightful summary that reflects the true intent of each subtask as described. Focus only on findings directly aligned with those subtasks—avoid speculation, off-topic commentary, or excessive generalization.

Level: **{size}**
Instructions: {instructions[size]}

Provide a clear and well-organized summary with the following sections:

1. **Key Points**
   - Present the most relevant insights that emerged from the entire research effort.
   - Use bullet points and concise language to highlight actionable insights.

2. **Comparison** (if applicable)
   - Briefly compare differing or similar findings across subtasks.

3. **Final Recommendation** (if applicable)
   - Offer a practical next step or synthesis based on the findings.

4. **Resources**
   - Cite any sources, links, or references if present in the content. Use the format:
     [Source: https://example.com], [Document: document.pdf]

Research Content:
{content}
"""

    return gemini_chat(prompt)
