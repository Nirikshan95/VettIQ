from langchain_core.prompts import PromptTemplate
from state.agent_state import AgentState
from models.chat_model import llm_with_tools
from tools.web_search_tool import web_search
from config import MARKET_ANALYST_PROMPT_PATH

def analyze_market(state:AgentState)->AgentState:
    """
    Creates a market analyst agent that can analyze market trends and provide insights.
    """
    try:
        template=open(MARKET_ANALYST_PROMPT_PATH).read()
    except FileNotFoundError:
        raise ValueError(f"Prompt file not found at {MARKET_ANALYST_PROMPT_PATH}. Please check the path and try again.")
    
    try: 
        prompt_template = PromptTemplate(
            input_variables=["startup_idea"],
            template=template
        )
        prompt=prompt_template.invoke({"startup_idea":state["startup_idea"]})
        response=llm_with_tools.invoke(prompt)
        return {"market_analysis": response.content}            
    except Exception as e:
        raise ValueError(f"Error analyzing market : {e}")