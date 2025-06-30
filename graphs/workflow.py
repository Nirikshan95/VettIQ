from langgraph.graph import StateGraph,END
from langgraph_supervisor import create_supervisor
from pydantic import BaseModel
from agents.market_analyst import market_analyst_agent
from agents.competitor_analysis import competitor_analysis_agent
from agents.risk_assessor import risk_assessor_agent
from agents.advisor import advisor_agent


class AgentState(BaseModel):
    messages: list[str]

supervisor_agent=create_supervisor(
        agents=[
            market_analyst_agent(),
            competitor_analysis_agent(),
            risk_assessor_agent(),
            advisor_agent(),
        ],
        name="Supervisor agent",
        description="This agent supervises the market analysis process, coordinating between different agents to ensure comprehensive insights.",
        prompt="You are a supervisor agent. Your task is to oversee the market analysis and  Startup Idea Vetting Assistant"
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

