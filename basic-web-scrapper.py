# Problem Statement
# Write Basic Web-Scrapper Project in Python

import requests
from bs4 import BeautifulSoup

# Function to scrape data
def scrape_data(url):
    try:
        # Fetch the HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Scraping all the headlines from a news site
        headlines = []
        for h2 in soup.find_all('h2'):
            headlines.append(h2.get_text())

        return headlines

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Usage
if __name__ == "__main__":
    url = 'https://example.com'  # Replace with the target URL
    headlines = scrape_data(url)
    print('Headlines:', headlines)
