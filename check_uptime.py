import requests
import time
from datetime import datetime

# --- CONFIGURATION ---

# 1. Add the websites you want to monitor.
#    (Must include "http://" or "https://")
WEBSITES_TO_CHECK = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.thissitedoesnotexist.com", # A known bad site for testing
]

# 2. Set the time to wait between checks (in seconds).
CHECK_INTERVAL = 60  # 60 seconds = 1 minute

# 3. Set the connection timeout (in seconds).
#    How long to wait for a site to respond before giving up.
TIMEOUT = 5
# ---------------------


def check_website(url):
    """
    Checks a single website for its status.
    Returns (True, "UP") if successful, (False, "DOWN") if not.
    """
    try:
        # 1. Send an HTTP GET request to the URL.
        #    We use a timeout to prevent the script from hanging on a non-responsive site.
        response = requests.get(url, timeout=TIMEOUT)
        
        # 2. Check the HTTP status code.
        #    Codes in the 200-299 range generally mean "success".
        if response.status_code >= 200 and response.status_code < 300:
            return (True, f"UP (Status: {response.status_code})")
        else:
            # Site is reachable but returned a client/server error code
            return (False, f"DOWN (Status: {response.status_code})")
            
    except requests.exceptions.Timeout:
        # The request timed out
        return (False, "DOWN (Error: Timeout)")
    except requests.exceptions.ConnectionError:
        # DNS failure, refused connection, etc.
        return (False, "DOWN (Error: Connection Failed)")
    except requests.exceptions.RequestException as e:
        # Catch any other request-related error
        return (False, f"DOWN (Error: {e})")

def main():
    """
    Main loop to continuously check websites.
    """
    print("--- Website Uptime Checker Started ---")
    while True:
        print("\n" + "="*30)
        
        # Get the current time for the timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Running check at: {current_time}")
        print("-" * 30)
        
        for url in WEBSITES_TO_CHECK:
            # 1. Check the site's status
            is_up, status_message = check_website(url)
            
            # 2. Format the output
            #    We use string formatting to make the columns align
            url_display = f"{url:<35}" # Pad the URL to 35 characters
            
            if is_up:
                print(f"{url_display} | STATUS: {status_message}")
            else:
                # Print "DOWN" messages in a more prominent way (optional)
                print(f"!!! {url_display} | STATUS: {status_message} !!!")
        
        # Wait for the defined interval before running the loop again
        print(f"\nWaiting for {CHECK_INTERVAL} seconds...")
        try:
            time.sleep(CHECK_INTERVAL)
        except KeyboardInterrupt:
            # Allow the user to stop the script with Ctrl+C
            print("\n--- Website Uptime Checker Stopped ---")
            break

if __name__ == "__main__":
    main()
