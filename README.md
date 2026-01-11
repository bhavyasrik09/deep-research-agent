
# 🧠 Deep Research Agent

**Multi-agent research system with critic-driven iteration**

Deep Research Agent is an AI-powered research assistant that automates research tasks using a loop of specialized agents: Planner, Researcher, Synthesizer, and Critic. The Critic ensures quality by iteratively refining the report until it meets high standards.

---

## ⚡ Features

* **Planner Agent**: Generates a structured research plan from a given topic.
* **Researcher Agent**: Performs web searches to collect notes and sources.
* **Synthesizer Agent**: Compiles research notes into a professional report.
* **Critic Agent**: Reviews the report and drives improvements iteratively.
* **Iteration Timeline**: Tracks multiple research iterations for transparency.
* **Sources & Citations Panel**: Displays all references for each iteration.
* **Export Options**: Markdown and PDF exports of the final report.
* **Interactive UI**: Streamlit-based interface for easy topic input and report viewing.

---

## 🛠️ Tech Stack

* **Python 3.13+**
* **Streamlit** — Frontend interface
* **Langgraph** — Multi-agent orchestration
* **LangChain Ollama** — LLM integration for planning, synthesizing, and critique
* **DDGS** — DuckDuckGo search API
* **FPDF** — PDF export

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/bhavyasrik09/deep-research-agent.git
cd deep-research-agent
```

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app locally

```bash
streamlit run ui/app.py
```

---

## 🧩 Usage

1. Enter your research topic in the input box.
2. Click **Run Research**.
3. View the **Final Report Timeline**, including all iterations.
4. Check **Critique** for improvement notes.
5. Export report as **Markdown** or **PDF** (if implemented).

---

## 📁 Project Structure

```
deep-research-agent/
├─ agents/
│  ├─ planner.py
│  ├─ researcher.py
│  ├─ synthesizer.py
│  └─ critic.py
├─ tools/
│  ├─ state.py
│  └─ web_search.py
├─ ui/
│  └─ app.py
├─ main.py
├─ requirements.txt
└─ README.md
```

---

## 💡 Future Enhancements

* Hackathon pitch slides & diagram
* Advanced citation formatting (APA/MLA)
* Integration with additional data sources & APIs
* Deployment on cloud platforms (Streamlit Cloud, Heroku, or AWS)

---

## 📄 License

MIT License

---
