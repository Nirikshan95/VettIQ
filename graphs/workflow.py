from langgraph.graph import StateGraph,END
from state.agent_state import AgentState
from nodes.market_analyst import analyze_market
from nodes.competitor_analysis import analyze_competition
from nodes.risk_assessor import assess_risk
from nodes.advisor import advisor


def build_graph():
    graph_builder = StateGraph(AgentState)
    
    #define the nodes
    graph_builder.add_node("analyze_market",analyze_market)
    graph_builder.add_node("analyze_competition",analyze_competition)
    graph_builder.add_node("assess_risk",assess_risk)
    graph_builder.add_node("advisor", advisor)
    
    graph_builder.set_entry_point("analyze_market")
    graph_builder.add_edge("analyze_market","analyze_competition")
    graph_builder.add_edge("analyze_competition","assess_risk")
    graph_builder.add_edge("assess_risk","advisor")
    graph_builder.add_edge("advisor", END)
    
    return graph_builder.compile()

