# Web scraping utilities for extracting data from websites


import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup


def extract_abstract_from_website(url):
    """
    Extracts the abstract from a given website URL and validates it using Ollama.
    :param url: The URL of the website
    :return: The validated abstract or None if validation fails
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

    
        # Attempt to find the abstract in all text or paragraph tags or divs
        paragraphs = soup.find_all(["p", "div"])
        abstract = next((p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)), None)
        # cut off abstract to be less then 1024 characters
        if abstract and len(abstract) > 1024:
            abstract = abstract[:1024]  # truncate abstract to 1024 characters
        if abstract:
            validation_response = requests.post(
                "http://ollama:11434/api/generate",
                json={
                "model": "gemma3:1b",
                "prompt": f"Is this an abstract? {abstract}. Answer strictly yes or no.",
                "max_tokens": 1,
                "options": {
                    "num_ctx": 2048
                }
                },
            )
            validation_response.raise_for_status()
            validation_text = validation_response.json().get("text", "").strip().lower()
            is_valid = validation_text == "yes"
            is_valid = validation_response.json().get("is_valid", False)
            if not is_valid:
                return None
            
    except requests.RequestException as e:
        print(f"Error fetching or validating URL {url}: {e}")
        return None
