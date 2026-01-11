from langchain_ollama import OllamaLLM
from tools.state import ResearchState

llm = OllamaLLM(model="mistral")


def critic_agent(state: ResearchState) -> ResearchState:
    prompt = f"""
You are a strict research reviewer.

1. Identify missing information or weak points.
2. Decide if the report needs improvement.

If improvement is needed, say YES.
If the report is good, say NO.

Respond in this format:

DECISION: YES or NO
CRITIQUE:
<your critique>

Report:
{state.get('report', '')}
"""

    response = llm.invoke(prompt)

    needs_improvement = "DECISION: YES" in response

    # Increment iteration only if further improvement is needed
    iteration = state.get("iteration", 1)
    if needs_improvement:
        iteration += 1

    return {
        **state,
        "needs_improvement": needs_improvement,
        "critique": response,
        "iteration": iteration,
    }
