from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal,Annotated
from state.agent_state import AgentState
from models.chat_model import llm_with_tools
from config import ADVISOR_PROMPT_PATH
import os

class AdvisorSchema(BaseModel):
    """
    Schema for the advisor response.
    """
    advisor_recommendations: Annotated[Literal["Go","No-Go","Conditional Go"], Field(description="The decision made by the advisor based on the analysis. whether to proceed with the startup idea or not.")]
    advice: Annotated[str,Field(description="Advice or suggestions or reasons provided by the advisor based on the analysis. This should include why the decision is 'Go' or 'Conditional Go', or reasons for 'No-Go'.")]
    
parser=PydanticOutputParser(pydantic_object=AdvisorSchema)
def advisor(state:AgentState)-> AgentState:
    """
    Analyzes market,competition ,risk and provides the advice.
    """
    if not os.path.exists(ADVISOR_PROMPT_PATH):
        raise ValueError(f"Prompt file not found at {ADVISOR_PROMPT_PATH}. Please check the path and try again.")
    
    try: 
        template=open(ADVISOR_PROMPT_PATH).read()
        prompt_template = PromptTemplate(
            input_variables=["startup_idea","market_analysis", "competition_analysis", "risk_assessment"],
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        chain=prompt_template | llm_with_tools | parser
        response=chain.invoke({"startup_idea":state["startup_idea"],"market_analysis":state["market_analysis"], "competition_analysis":state["competition_analysis"], "risk_assessment":state["risk_assessment"]})
        return {"advisor_recommendations": response.advisor_recommendations,"advice": response.advice}
        
    except Exception as e:
        raise ValueError(f"Error  advising : {e}")