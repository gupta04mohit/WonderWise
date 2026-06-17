from langchain_community.utilities import GoogleSerperAPIWrapper

def google_search(query: str) -> str:
    search = GoogleSerperAPIWrapper()
    return search.run(query)

    