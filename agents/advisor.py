from langgraph.prebuilt import create_react_agent
from models.chat_model import load_chat_model
from tools.web_search_tool import web_search

def advisor_agent():
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    return create_react_agent(
        name="advisor",
        model=load_chat_model(),
        tools=[web_search],
        prompt="You are a startup advisor. Given the entire context, recommend whether to proceed, not proceed, or conditionally proceed. Provide clear reasons."
    )
