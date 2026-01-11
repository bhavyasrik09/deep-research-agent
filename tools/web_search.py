from ddgs import DDGS
from ddgs.exceptions import TimeoutException

def search_web(query: str, max_results: int = 5):
    """
    Perform a DuckDuckGo search and return a list of dicts:
    [{"title": ..., "url": ...}, ...]
    Safe version with timeout handling.
    """
    results = []
    try:
        with DDGS(timeout=30) as ddgs:  # 30s timeout
            for r in ddgs.text(query, backend="api", max_results=max_results):
                results.append({
                    "title": r.get("title", "No title"),
                    "url": r.get("href", "")
                })
    except TimeoutException:
        print("⚠️ Search timed out. Returning empty results.")
    except Exception as e:
        print(f"⚠️ Search failed: {e}")
    return results
