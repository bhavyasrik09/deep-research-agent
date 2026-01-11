from tools.web_search import search_web
from tools.state import ResearchState

MAX_QUERY_LENGTH = 300  # max characters to send to DuckDuckGo

def researcher_agent(state: ResearchState) -> ResearchState:
    notes = state.get("notes", [])
    sources = state.get("sources", [])
    iteration = state.get("iteration", 1)

    # First pass → topic
    # Later passes → critique-driven refinement
    focus_query = state["topic"] if iteration == 1 else state.get("critique", state["topic"])

    for step in state.get("plan", []):
        # Construct query but truncate to avoid long URLs
        query = f"{focus_query} {step}"
        if len(query) > MAX_QUERY_LENGTH:
            query = query[:MAX_QUERY_LENGTH] + "..."  # truncate and add ellipsis

        # Perform search safely
        try:
            results = search_web(query)
        except Exception as e:
            print(f"⚠️ Search failed for query: {query} | Error: {e}")
            results = []

        # Add results to notes
        notes.extend(results)

        # Save URLs as sources
        for r in results:
            url = r.get("url")
            if url and url not in sources:
                sources.append(url)

    state["notes"] = notes
    state["sources"] = sources

    # Save a snapshot of this iteration
    if "reports" not in state:
        state["reports"] = []
    state["reports"].append({
        "iteration": iteration,
        "report": state.get("report", ""),
        "sources": sources.copy()
    })

    return state
