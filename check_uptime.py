import requests
import time
from datetime import datetime

WEBSITES_TO_CHECK = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.thissitedoesnotexist.com",
]
CHECK_INTERVAL = 60
TIMEOUT = 5

def check_website(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if 200 <= response.status_code < 300:
            return (True, f"UP ({response.status_code})")
        else:
            return (False, f"DOWN ({response.status_code})")
    except Exception as e:
        return (False, f"DOWN ({e})")

def main():
    print("--- Website Uptime Checker Started ---")
    while True:
        print(f"\nCheck time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for url in WEBSITES_TO_CHECK:
            is_up, msg = check_website(url)
            print(f"{url:<35} | STATUS: {msg}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
