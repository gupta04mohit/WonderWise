from langgraph.graph import StateGraph, END
from state import TravelState
from agents.destination import destination_agent
from agents.experiences import experiences_agent
from agents.itinerary import itinerary_agent

def build_graph():
    g = StateGraph(TravelState)
    g.add_node("destination", destination_agent)
    g.add_node("experiences", experiences_agent)
    g.add_node("itinerary", itinerary_agent)

    g.set_entry_point("destination")
    g.add_edge("destination", "experiences")
    g.add_edge("experiences", "itinerary")
    g.add_edge("itinerary", END)
    return g.compile()

    