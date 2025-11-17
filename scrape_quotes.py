import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/"

def main():
    '''Scrapes quotes from the target URL.'''
    print(f"Scraping quotes from: {URL}")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.find_all("div", class_="quote")
        
        if not quote_elements:
            print("No quotes found.")
            return

        for i, quote in enumerate(quote_elements):
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            print(f"Quote {i + 1}:\n{text}\n - {author}\n")
            print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
