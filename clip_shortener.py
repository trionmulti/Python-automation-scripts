import pyperclip
import requests
import time
import re

CHECK_INTERVAL = 2
TINYURL_API = "http://tinyurl.com/api-create.php"

def shorten(url):
    try:
        return requests.get(TINYURL_API, params={'url': url}).text
    except: return None

def main():
    print("Clipboard Shortener running (Ctrl+C to stop)")
    last_clip = ""
    while True:
        clip = pyperclip.paste()
        if clip != last_clip:
            if re.match(r'^https?://(?!tinyurl\.com)', clip):
                short = shorten(clip)
                if short:
                    pyperclip.copy(short)
                    print(f"Shortened: {short}")
                    last_clip = short
                    continue
            last_clip = clip
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
