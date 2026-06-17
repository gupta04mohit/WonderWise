from dotenv import load_dotenv
load_dotenv() 
from langchain_groq import ChatGroq
from tools.google_search import google_search


def experiences_agent(state: dict) -> dict:
    """
    Recommends attractions, food, cultural spots, and activities
    based on user interests and destination city.
    """

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.1
    )

    # Build research query
    query = (
        f"Top attractions, food, culture, and activities in "
        f"{state['destination_city']} for interests: {state['interests']}."
    )

    # Perform web search
    research = google_search(query)

    # Generate curated experiences list
    response = llm.invoke(
        f"""
        Using the following research data:

        {research}

        Create a curated, traveler-friendly list of experiences.
        Organize the output into clear sections such as:
        - Must-see attractions
        - Local food & dining
        - Cultural experiences
        - Hidden gems

        Use bullet points where appropriate.
        """
    )

    # Update shared graph state
    state["experiences"] = response.content

    return state


