AI-Powered Research Assistant

(Multi-Agent + RAG + Gemini 2.5)

Mohammed Medhat

**Overview** 

An intelligent multi-agent system that automates research, comparison, and summarization of technical topics using Google’s Gemini 2.5 Flash and a user-friendly Streamlit interface. 

**1  Features** 

- **Modular AI agents** for research, comparison, and final synthesis 
- **Summarization options**: Small (brief), Medium (standard), Large (detailed) 
- **Automatic RAG-style workflow**: Each agent gathers data, which is then summarized 
- **Sources and insights** included at the end 
- Built with Streamlit for a clean, interactive UI 

**2  Use Cases** 

- Compare APIs, tools, frameworks 
- Quickly generate decision-ready technical summaries 
- Save hours of manual research time 

**3  Tech Stack** 

- **LLM**:  Gemini  2.5  Flash  API  (via  gemini*chat*)**Orchestration**  : *Customagent*−*basedpipeline*(*Planne* 
- **UI**: Streamlit with detail-level selector 
- **RAG**: Manual multi-agent retrieval + LLM summarization 

1 

AI-Powered Research Assistant  July 23, 2025 ![](Aspose.Words.3ad49c47-601c-450b-b5d2-d9090b285a03.001.png)

**4  RAG Architecture (Simplified)** 

User Prompt Planner [Research Agents] Synthesizer Summarizer Final Answer 

Task-specific  Gemini Summary Content Fetch  (Small / Medium / Large) 

**5  Motivation** 

This project was developed to deepen my understanding of multi-agent systems, leveraging a modular design to explore AI agent orchestration, retrieval-augmented generation (RAG), and practical application development. 
