import streamlit as st
from agents.planner import plan_task
from agents.researcher import run_research
from agents.summarizer import summarize_content

st.set_page_config(page_title="Intelligent AI Agent", layout="wide")
st.title("🧠 Intelligent Research Agent")
st.markdown("Give it a task — it will break it down, research each part, and give you a final report!")

# Input: research task
task = st.text_input("🔍 What do you want to research?", "")

# Output size selection
summary_size = st.radio(
    "📝 Select output size (detail level):",
    ["Small", "Medium", "Large"],
    index=1,
    help="Choose how detailed the final report should be."
)

# Run button
if st.button("Run") and task.strip():
    with st.spinner(f"📚 Summarizing findings ({summary_size})..."):
    #with st.spinner("🧠 Planning subtasks..."):
        subtasks = plan_task(task)
     #   st.success("✅ Subtasks planned:")
      #  for s in subtasks:
       #     st.write("•", s)

        results = []
        for sub in subtasks:
        #with st.spinner(f"🔎 Researching: {sub}"):
            result = run_research(sub)
            results.append(result)
         #   st.success(f"✅ Done: {sub}")
        #  st.markdown(result['content'][:500] + "...")

    
        summary = summarize_content(results, summary_size)

    st.subheader("📄 Final Report")
    st.markdown(summary)

    st.download_button("📥 Download Report as TXT", summary, file_name="final_report.txt")
