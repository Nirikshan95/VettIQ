from langchain_core.prompts import PromptTemplate
from state.agent_state import AgentState
from models.chat_model import llm_with_tools
from config import COMPETITOR_ANALYSIS_PROMPT_PATH

def analyze_competition(state: AgentState):
    """
    analyzes competition and provide insights.
    """
    try:
        template = open(COMPETITOR_ANALYSIS_PROMPT_PATH).read()
    except FileNotFoundError:
        raise ValueError(f"Prompt file not found at {COMPETITOR_ANALYSIS_PROMPT_PATH}. Please check the path and try again.")

    try: 
        prompt_template = PromptTemplate(
            input_variables=["startup_idea","market_analysis"],
            template=template
        )
        prompt=prompt_template.invoke({"startup_idea":state["startup_idea"],"market_analysis":state["market_analysis"]})
        response=llm_with_tools.invoke(prompt)
        return {"competition_analysis": response.content}
        
    except Exception as e:
        raise ValueError(f"Error analyzing competition : {e}")