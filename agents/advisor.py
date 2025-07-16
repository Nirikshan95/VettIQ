from langgraph.prebuilt import create_react_agent
from tools.web_search_tool import web_search
from config import ADVISOR_PROMPT_PATH
import os

def advisor_agent(llm):
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    placeholder_prompt = "You are a startup advisor. Given the entire context, recommend whether to proceed, not proceed, or conditionally proceed. Provide clear reasons."
    return create_react_agent(
        name="advisor",
        model=llm,
        tools=[web_search],
        prompt=open(ADVISOR_PROMPT_PATH).read() if os.path.exists(ADVISOR_PROMPT_PATH) else placeholder_prompt
        )
