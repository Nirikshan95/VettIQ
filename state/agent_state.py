from typing import TypedDict

#State model for the agent
class AgentState(TypedDict):
    startup_idea: str
    market_analysis: str
    competition_analysis: str
    risk_assessment: str
    advisor_recommendations: str
    advice:str