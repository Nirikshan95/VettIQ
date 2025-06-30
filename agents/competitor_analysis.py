from langgraph.prebuilt import create_react_agent
from models.chat_model import load_chat_model
from tools.web_search_tool import web_search

def competitor_analyst_agent():
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    return create_react_agent(
        name="competitor_analyst",
        model=load_chat_model(),
        tools=[web_search],
        prompt="You are a competitive intelligence analyst. Given this idea and the market analysis, list major competitors, their features, pricing, and suggest potential differentiators."
    )