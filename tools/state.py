from typing import TypedDict, List


class ResearchState(TypedDict):
    topic: str
    plan: List[str]
    notes: List[str]
    report: str
    critique: str
    needs_improvement: bool
    iteration: int
    sources: List[str] 
