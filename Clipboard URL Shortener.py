import pyperclip
import requests
import time
import re

# --- CONFIGURATION ---

# 1. How often to check the clipboard (in seconds).
#    A lower number is faster but uses more resources.
CHECK_INTERVAL = 2  # 2 seconds

# 2. TinyURL API endpoint (no key needed)
TINYURL_API_URL = "http://tinyurl.com/api-create.php"
# ---------------------


def shorten_url(long_url):
    """
    Uses the TinyURL API to shorten a given URL.
    Returns the short URL string, or None if it fails.
    """
    try:
        # The API is simple: just pass the URL as a parameter
        payload = {'url': long_url}
        response = requests.get(TINYURL_API_URL, params=payload)
        
        response.raise_for_status() # Check for HTTP errors
        
        # The API returns the short URL as plain text
        return response.text
        
    except requests.exceptions.RequestException as e:
        # Handle network errors, timeouts, etc.
        print(f"Error shortening URL: {e}")
        return None

def is_url(text):
    """
    Checks if a string is a valid-looking URL.
    Also ensures it's not already a tinyurl.
    """
    # A simple regex to check for http/https and not tinyurl.com
    url_pattern = re.compile(r'^https?://(?!tinyurl\.com/)\S+$', re.IGNORECASE)
    return bool(url_pattern.match(text))

def main():
    """
    Main loop to monitor the clipboard.
    """
    print("--- Clipboard URL Shortener Started ---")
    print("Monitoring clipboard... (Press Ctrl+C to stop)")
    
    # We need to store the last thing we copied to avoid
    # re-shortening something we just put on the clipboard.
    last_clipboard_content = ""

    try:
        while True:
            # 1. Get current clipboard content
            current_clipboard = pyperclip.paste()
            
            # 2. Check if it's new and if it's a URL
            if (current_clipboard != last_clipboard_content and 
                is_url(current_clipboard)):
                
                print(f"Detected URL: {current_clipboard}")
                
                # 3. Shorten the URL
                short_url = shorten_url(current_clipboard)
                
                if short_url:
                    print(f"Shortened: {short_url}")
                    
                    # 4. Copy the short URL back to the clipboard
                    pyperclip.copy(short_url)
                    
                    # 5. Update our 'last' content to be the new short URL
                    last_clipboard_content = short_url
                else:
                    # If shortening fails, update 'last' content anyway
                    # so we don't keep trying to shorten the bad URL
                    last_clipboard_content = current_clipboard
            
            elif current_clipboard != last_clipboard_content:
                # It's new content, but not a URL. Just log it.
                last_clipboard_content = current_clipboard

            # 6. Wait before checking again
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n--- Clipboard URL Shortener Stopped ---")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
