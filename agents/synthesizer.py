from langchain_ollama import OllamaLLM
from tools.state import ResearchState

llm = OllamaLLM(model="mistral")


def synthesizer_agent(state: ResearchState) -> ResearchState:
    """
    Generate a professional report from research notes.
    Appends report for each iteration to allow timeline display.
    """
    iteration = state.get("iteration", 1)
    topic = state.get("topic", "")
    notes = state.get("notes", [])

    prompt = f"""
Write a professional research report on the topic below.

Topic:
{topic}

Research Notes:
{notes}

Structure:
- Introduction
- Key Findings
- Conclusion
"""

    report_text = llm.invoke(prompt)

    # Store reports per iteration in a list
    reports = state.get("reports", [])
    reports.append({"iteration": iteration, "report": report_text})

    # Update main report to latest
    state["report"] = report_text
    state["reports"] = reports

    return state
