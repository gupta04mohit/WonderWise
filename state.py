from typing import TypedDict, Dict, Any

class TravelState(TypedDict, total=False):
    from_city: str
    destination_city: str
    interests: str
    start_date: str
    end_date: str
    destination_info: str
    experiences: str
    itinerary: str

    