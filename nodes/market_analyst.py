from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated
from state.agent_state import AgentState
from models.chat_model import llm_with_tools
from tools.web_search_tool import web_search
from config import MARKET_ANALYST_PROMPT_PATH

# Scheama for market analyst response
class MarketAnalysisSchema(BaseModel):
    """
    Schema for the market analysis response.
    """
    market_analysis: Annotated[str, Field(description="Market analysis insights based on the startup idea.")]


def analyze_market(state:AgentState)->AgentState:
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    try:
        template=open(MARKET_ANALYST_PROMPT_PATH).read()
    except FileNotFoundError:
        raise ValueError(f"Prompt file not found at {MARKET_ANALYST_PROMPT_PATH}. Please check the path and try again.")
    
    try: 
        parser = PydanticOutputParser(pydantic_object=MarketAnalysisSchema)         #parser for the market analysis response
        prompt_template = PromptTemplate(
            input_variables=["startup_idea"],
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        chain = prompt_template | llm_with_tools | parser
        response=chain.invoke({"startup_idea":state["startup_idea"]})
        return {"market_analysis": response.market_analysis}            
    except Exception as e:
        raise ValueError(f"Error analyzing market : {e}")