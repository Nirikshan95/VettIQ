from langchain_core.prompts import PromptTemplate
from state.agent_state import AgentState
from models.chat_model import llm_with_tools
import os
from tools.web_search_tool import web_search
from config import RISK_ASSESSOR_PROMPT_PATH

def assess_risk(state: AgentState) -> AgentState:
    """
    Analyzes risk factors and provide trends and insights.
    """
    if not os.path.exists(RISK_ASSESSOR_PROMPT_PATH):
        raise FileNotFoundError(f"Prompt file not found at {RISK_ASSESSOR_PROMPT_PATH}. Please check the path and try again.")
    try:
        template = open(RISK_ASSESSOR_PROMPT_PATH).read()
        prompt_template = PromptTemplate(
            input_variables=["startup_idea", "market_analysis", "competition_analysis"],
            template=template
        )
        prompt = prompt_template.invoke({
            "startup_idea": state["startup_idea"],
            "market_analysis": state["market_analysis"],
            "competition_analysis": state["competition_analysis"]
        })
        response = llm_with_tools.invoke(prompt)
        return {"risk_assessment": response.content}
    except Exception as e:
        raise ValueError(f"Error analyzing risk: {e}")