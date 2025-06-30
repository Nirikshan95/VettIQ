from langgraph.prebuilt import create_react_agent
from models.chat_model import load_chat_model
from tools.web_search_tool import web_search

def risk_assessort_agent():
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    return create_react_agent(
        name="risk Analyst",
        model=load_chat_model(),
        tools=[web_search],
        prompt="You are a risk assessment expert. Based on this idea, market analysis, and competitor analysis, identify potential risks and suggest mitigations."
    )