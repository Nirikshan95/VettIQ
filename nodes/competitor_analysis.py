from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated
from state.agent_state import AgentState
from models.chat_model import llm_with_tools
from config import COMPETITOR_ANALYSIS_PROMPT_PATH

# Schema for competitor analysis response
class CompetitorAnalysisSchema(BaseModel):
    """
    Schema for the competitor analysis response.
    """
    competition_analysis: Annotated[str, Field(description="Insights on the competition based on the startup idea and market analysis.")]


def analyze_competition(state: AgentState):
    """
    analyzes competition and provide insights.
    """
    try:
        template = open(COMPETITOR_ANALYSIS_PROMPT_PATH).read()
    except FileNotFoundError:
        raise ValueError(f"Prompt file not found at {COMPETITOR_ANALYSIS_PROMPT_PATH}. Please check the path and try again.")

    try:
        parser = PydanticOutputParser(pydantic_object=CompetitorAnalysisSchema)  # parser for the competitor analysis response
        # Create a prompt template for the competitor analysis 
        prompt_template = PromptTemplate(
            input_variables=["startup_idea","market_analysis"],
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        competition_analysis_chain = prompt_template | llm_with_tools | parser
        response=competition_analysis_chain.invoke({"startup_idea":state["startup_idea"],"market_analysis":state["market_analysis"]})
        return {"competition_analysis": response.competition_analysis}
        
    except Exception as e:
        raise ValueError(f"Error analyzing competition : {e}")