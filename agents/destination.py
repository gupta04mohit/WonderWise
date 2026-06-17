from dotenv import load_dotenv
load_dotenv()  

from langchain_groq import ChatGroq
from tools.google_search import google_search


def destination_agent(state: dict) -> dict:
    """
    Researches destination-level information such as:
    - City overview
    - Weather during travel dates
    - Best time to visit
    - Practical travel tips
    """

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    # Build research query
    query = (
        f"Provide an overview, expected weather, best time to visit, "
        f"and important travel tips for {state['destination_city']} "
        f"between {state['start_date']} and {state['end_date']}."
    )

    # Perform web search
    research = google_search(query)

    # Summarize research using LLM
    response = llm.invoke(
        f"""
        Using the following research data:

        {research}

        Create a concise, traveler-friendly summary.
        """
    )

    # Update shared state
    state["destination_info"] = response.content

    return state
 

 