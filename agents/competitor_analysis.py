from langgraph.prebuilt import create_react_agent
import os
from tools.web_search_tool import web_search
from config import COMPETITOR_ANALYSIS_PROMPT_PATH

def competitor_analyst_agent(llm):
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    placeholder_prompt="You are a competitive intelligence analyst. Given this idea and the market analysis, list major competitors, their features, pricing, and suggest potential differentiators."

    return create_react_agent(
        name="competitor_analyst",
        model=llm,
        tools=[web_search],
        prompt=open(COMPETITOR_ANALYSIS_PROMPT_PATH).read() if os.path.exists(COMPETITOR_ANALYSIS_PROMPT_PATH) else placeholder_prompt
        )