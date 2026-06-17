from dotenv import load_dotenv
load_dotenv()  

from langchain_groq import ChatGroq


def itinerary_agent(state: dict) -> dict:
    """
    Synthesizes destination research and experiences into
    a structured, day-by-day travel itinerary.
    """

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = f"""
    Create a detailed, day-by-day travel itinerary for a trip
    from {state['start_date']} to {state['end_date']} in
    {state['destination_city']}.

    Use the following information:

    Destination Information:
    {state.get('destination_info', '')}

    Experiences & Attractions:
    {state.get('experiences', '')}

    Guidelines:
    - Break the plan into clear daily sections (Day 1, Day 2, etc.)
    - Include activities for morning, afternoon, and evening
    - Keep the plan realistic and traveler-friendly
    - Use bullet points and concise descriptions
    - Do NOT hallucinate places; rely on provided info
    """

    response = llm.invoke(prompt)

    # Update shared graph state
    state["itinerary"] = response.content

    return state


