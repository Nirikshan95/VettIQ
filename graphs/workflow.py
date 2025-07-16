from langgraph.graph import StateGraph,END
from langgraph_supervisor import create_supervisor
import os
from pydantic import BaseModel
from models.chat_model import load_chat_model
from agents.market_analyst import market_analyst_agent
from agents.competitor_analysis import competitor_analysis_agent
from agents.risk_assessor import risk_assessor_agent
from agents.advisor import advisor_agent
from config import SUPERVISOR_PROMPT_PATH
#State model for the agent
class AgentState(BaseModel):
    messages: list[str]
    
chat_model=load_chat_model()        #llm 
supervisor_placeholder_prompt="You are a supervisor agent. Your task is to oversee the market analysis and  Startup Idea Vetting Assistant"
supervisor_agent=create_supervisor(
        agents=[
            market_analyst_agent(llm=chat_model),
            competitor_analysis_agent(llm=chat_model),
            risk_assessor_agent(llm=chat_model),
            advisor_agent(llm=chat_model),
        ],
        name="Supervisor agent",
        description="This agent supervises the market analysis process, coordinating between different agents to ensure comprehensive insights.",
        prompt=open(SUPERVISOR_PROMPT_PATH).read() if os.path.exists(SUPERVISOR_PROMPT_PATH) else supervisor_placeholder_prompt
        )

def supervisor(state: AgentState) -> dict:
    
    return {"messages": supervisor_agent.invoke(state.messages)}

def build_graph():
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node(
        "idea_vetting",
        supervisor
    )
    graph_builder.set_entry_point("idea_vetting")
    graph_builder.add_edge("idea_vetting",END)
    return graph_builder.compile()

