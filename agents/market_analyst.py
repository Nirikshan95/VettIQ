from langgraph.prebuilt import create_react_agent
import os
from tools.web_search_tool import web_search
from config import MARKET_ANALYST_PROMPT_PATH

def market_analyst_agent(llm):
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    placeholder_prompt="You are a market analyst. Your task is to analyze market trends and provide insights based on the data provided. Use your expertise to interpret the data and offer actionable recommendations."
    return create_react_agent(
        name="Market Analyst",
        model=llm,
        tools=[web_search],
        prompt=open(MARKET_ANALYST_PROMPT_PATH).read() if os.path.exists(MARKET_ANALYST_PROMPT_PATH) else placeholder_prompt
    )