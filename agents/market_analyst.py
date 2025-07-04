from langgraph.prebuilt import create_react_agent
from models.chat_model import load_chat_model
from tools.web_search_tool import web_search

def market_analyst_agent():
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    return create_react_agent(
        name="Market Analyst",
        model=load_chat_model(),
        tools=[web_search],
        prompt="You are a market analyst. Your task is to analyze market trends and provide insights based on the data provided. Use your expertise to interpret the data and offer actionable recommendations.",
    )