from langgraph.graph import StateGraph, END
from tools.state import ResearchState

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.synthesizer import synthesizer_agent
from agents.critic import critic_agent

MAX_ITERATIONS = 3


def should_continue(state: ResearchState) -> str:
    """
    Decide whether to loop back to researcher or end.
    """
    if state.get("needs_improvement", False) and state.get("iteration", 1) < MAX_ITERATIONS:
        state["iteration"] = state.get("iteration", 1) + 1
        return "researcher"
    return "end"


def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("synthesizer", synthesizer_agent)
    graph.add_node("critic", critic_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "synthesizer")
    graph.add_edge("synthesizer", "critic")

    graph.add_conditional_edges(
        "critic",
        should_continue,
        {
            "researcher": "researcher",
            "end": END,
        },
    )

    return graph.compile()


if __name__ == "__main__":
    app = build_graph()

    state: ResearchState = {
        "topic": "AI agents in healthcare",
        "plan": [],
        "notes": [],
        "report": "",
        "reports": [],  # stores iteration reports
        "sources": [],  # stores sources/citations
        "critique": "",
        "needs_improvement": True,
        "iteration": 1,
    }

    final_state = app.invoke(state)

    print("\n" + "=" * 50)
    print("FINAL REPORT TIMELINE")
    print("=" * 50)
    for r in final_state.get("reports", []):
        print(f"\n--- Iteration {r['iteration']} ---")
        print(r.get("report", ""))
        if r.get("sources"):
            print("Sources / Citations:")
            for s in r["sources"]:
                print("-", s)

    print("\n" + "=" * 50)
    print("FINAL CRITIQUE")
    print("=" * 50)
    print(final_state.get("critique", ""))
