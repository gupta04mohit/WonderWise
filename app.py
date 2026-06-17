from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
from datetime import date, timedelta

from graph import build_graph



# Page Configuration

st.set_page_config(
    page_title="WonderWise",
    page_icon="🧭",
    layout="wide"
)

st.title("🧭 WonderWise — Multi-Agent Travel Planner")
st.caption(
    "An agentic AI system where multiple specialized agents collaborate "
    "to generate a personalized travel itinerary."
)

st.divider()



# Input Section

with st.container(border=True):
    st.subheader("✍️ Travel Preferences")

    c1, c2 = st.columns(2)
    from_city = c1.text_input("From City", "Paris")
    destination_city = c2.text_input("Destination City", "London")

    interests = st.text_input(
        "Interests",
        "culture, food, history, local experiences"
    )

    d1, d2 = st.columns(2)
    start_date = d1.date_input("Start Date", date.today())
    end_date = d2.date_input("End Date", date.today() + timedelta(days=5))



# Validation

travel_days = (end_date - start_date).days

ready = (
    from_city.strip()
    and destination_city.strip()
    and interests.strip()
    and travel_days > 0
)

st.divider()

if ready:
    st.success(
        f"Planning a **{travel_days}-day trip** "
        f"from **{from_city}** to **{destination_city}**."
    )
else:
    st.warning(
        "Please complete all fields correctly "
        "and ensure the end date is after the start date."
    )


# Execution

if st.button(
    "🧠 Generate Intelligent Travel Plan",
    use_container_width=True,
    disabled=not ready
):
    with st.status(
        "🤖 Multi-agent system running...",
        state="running",
        expanded=True
    ):
        graph = build_graph()

        state = {
            "from_city": from_city,
            "destination_city": destination_city,
            "interests": interests,
            "start_date": str(start_date),
            "end_date": str(end_date),
        }

        result = graph.invoke(state)

    st.divider()
    st.subheader("🗺️ Final Itinerary")

    itinerary = result.get("itinerary")

    if itinerary:
        st.markdown(itinerary)
    else:
        st.error(
            "No itinerary was generated. "
            "Please try adjusting your inputs."
        )


# Footer

st.divider()
st.caption(
    "WonderWise • Multi-Agent AI using LangGraph + Groq "
    "• Stable LLaMA-3.1-8B"
)


