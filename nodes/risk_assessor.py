from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated
from state.agent_state import AgentState
from models.chat_model import llm_with_tools
import os
from tools.web_search_tool import web_search
from config import RISK_ASSESSOR_PROMPT_PATH

# Schema for risk assessment response
class RiskAssessmentSchema(BaseModel):
    """
    Schema for the risk assessment response.
    """
    risk_assessment: Annotated[str, Field(description="Risk assessment insights based on the startup idea, market analysis, and competition analysis.")]

def assess_risk(state: AgentState) -> AgentState:
    """
    Analyzes risk factors and provide trends and insights.
    """
    if not os.path.exists(RISK_ASSESSOR_PROMPT_PATH):
        raise FileNotFoundError(f"Prompt file not found at {RISK_ASSESSOR_PROMPT_PATH}. Please check the path and try again.")
    try:
        template = open(RISK_ASSESSOR_PROMPT_PATH).read()
        parser= PydanticOutputParser(pydantic_object=RiskAssessmentSchema)  # parser for the risk assessment response
        # Create a prompt template for the risk assessment
        prompt_template = PromptTemplate(
            input_variables=["startup_idea", "market_analysis", "competition_analysis"],
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        
        # Chain the prompt template with the LLM and parser
        risk_assessment_chain = prompt_template | llm_with_tools | parser
        response = risk_assessment_chain.invoke({
            "startup_idea": state["startup_idea"],
            "market_analysis": state["market_analysis"],
            "competition_analysis": state["competition_analysis"]
        })
        return {"risk_assessment": response.risk_assessment}
    except Exception as e:
        raise ValueError(f"Error analyzing risk: {e}")