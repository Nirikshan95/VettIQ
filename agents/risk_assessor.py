from langgraph.prebuilt import create_react_agent
import os
from tools.web_search_tool import web_search
from config import RISK_ASSESSOR_PROMPT_PATH

def risk_assessort_agent(llm):
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    placeholder_prompt = "You are a risk assessor. Given the entire context, evaluate the risks associated with the startup idea and provide a detailed risk assessment."
    return create_react_agent(
        name="risk Analyst",
        model=llm,
        tools=[web_search],
        prompt=open(RISK_ASSESSOR_PROMPT_PATH).read() if os.path.exists(RISK_ASSESSOR_PROMPT_PATH) else placeholder_prompt
    )