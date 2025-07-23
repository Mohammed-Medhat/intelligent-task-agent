import requests
from config import SERPAPI_API_KEY

def search_google(query):
    url = "https://serpapi.com/search"
    params = {"engine": "google", "q": query, "api_key": SERPAPI_API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    print(f"Search results for '{query}': {len(data.get('organic_results', []))} found.")
    return data.get("organic_results", [])

