import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser') 
    quotes = soup.find_all('span', class_='text')
    return [quote.get_text() for quote in quotes]

def main():
    main_url = "http://quotes.toscrape.com"
    example_paths = [
        "/tag/humor",
        "/tag/inspirational",
        "/tag/life",
        "/tag/love",
        "/tag/success",
    ]

    for path in example_paths:
        full_url = main_url + path
        data = fetch_data(full_url)

        if data is not None:
            extracted_data = extract_data(data)
            if extracted_data:
                print(f"Data from {full_url}:\n{extracted_data}\n{'='*30}")
            else:
                print(f"No data found on {full_url}\n{'='*30}")
                # Add logic to go back to the initial position if needed
        else:
            # Handle the case where data couldn't be fetched
            # You might want to implement a retry mechanism or other error handling here
            print(f"Failed to fetch data from {full_url}\n{'='*30}")

if '_name_' == "_main_":
    main()