from langgraph.graph import StateGraph,END
import os
from state.agent_state import AgentState
from nodes.market_analyst import analyze_market
from nodes.competitor_analysis import analyze_competition
from nodes.risk_assessor import assess_risk
from nodes.advisor import advisor
from config import GRAPH_VISUALIZATION_PATH


def build_graph():
    try:
        graph_builder = StateGraph(AgentState)
        
        # define the nodes
        graph_builder.add_node("analyze_market",analyze_market)
        graph_builder.add_node("analyze_competition",analyze_competition)
        graph_builder.add_node("assess_risk",assess_risk)
        graph_builder.add_node("advisor", advisor)
        
        graph_builder.set_entry_point("analyze_market")     # entry point of the graph
        
        graph_builder.add_edge("analyze_market","analyze_competition")
        graph_builder.add_edge("analyze_competition","assess_risk")
        graph_builder.add_edge("assess_risk","advisor")
        graph_builder.add_edge("advisor", END)
        
        graph=graph_builder.compile()       # compile the graph
        
        """#graph visualization
        try:
            graph_img_path=os.makedirs(GRAPH_VISUALIZATION_PATH,exist_ok=True)
            graph.get_graph().draw_mermaid_png(output_file_path=graph_img_path,padding=50,background_color="gray")
        except Exception as e:
            print(f"Error in graph visualization: {e}")
        """
        return graph
    except Exception as e:
        print(f"Error in building graph: {e}")
        return None