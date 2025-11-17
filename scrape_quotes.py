import requests
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
# The URL of the site we want to scrape
URL = "http://quotes.toscrape.com/"
# ---------------------


def main():
    """
    Main function to scrape quotes from the target URL.
    """
    print(f"Scraping quotes from: {URL}\n")
    
    try:
        # 1. Send the HTTP request to the URL
        response = requests.get(URL)
        
        # Raise an exception if the request was unsuccessful (e.g., 404, 500)
        response.raise_for_status()
        
        # 2. Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 3. Find all elements that contain a quote.
        #    (After inspecting the site, we know each quote is in a <div class="quote">)
        quote_elements = soup.find_all("div", class_="quote")
        
        if not quote_elements:
            print("No quotes found on the page.")
            return

        print(f"Found {len(quote_elements)} quotes:\n")
        print("-" * 30)

        # 4. Loop through each quote element and extract the data
        for i, quote in enumerate(quote_elements):
            # Find the text of the quote (in a <span class="text">)
            text = quote.find("span", class_="text").get_text()
            
            # Find the author (in a <small class="author">)
            author = quote.find("small", class_="author").get_text()
            
            # 5. Print the extracted data
            print(f"Quote {i + 1}:\n{text}\n - {author}\n")
            print("-" * 30)

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (DNS failure, connection refused, etc.)
        print(f"An error occurred during the web request: {e}")
    except Exception as e:
        # Handle other potential errors (e.g., parsing errors)
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
