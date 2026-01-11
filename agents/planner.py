from langchain_ollama import OllamaLLM
from tools.state import ResearchState

llm = OllamaLLM(model="mistral")


def planner_agent(state: ResearchState) -> ResearchState:
    prompt = f"""
You are a research planner.

Topic: {state['topic']}

Create a clear, 4-step research plan.
Return only bullet points.
"""

    response = llm.invoke(prompt)
    plan = [line.strip("- ").strip() for line in response.split("\n") if line.strip()]

    state["plan"] = plan
    return state
