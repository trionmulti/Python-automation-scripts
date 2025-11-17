# Python Automation Scripts 🐍

A collection of 11 practical Python scripts designed to automate daily tasks, manage files, manipulate data, and interact with APIs.

## 📂 Project Overview

| Script Name | Description | Dependencies |
| :--- | :--- | :--- |
| **`organize_files.py`** | Scans a folder and moves files into subfolders based on extension (Images, Docs, etc.). | `os`, `shutil` |
| **`scrape_quotes.py`** | Scrapes quotes and authors from *quotes.toscrape.com*. | `requests`, `bs4` |
| **`check_uptime.py`** | Monitors a list of websites and logs their UP/DOWN status. | `requests` |
| **`resize_images.py`** | Bulk resizes images in a folder to a maximum dimension. | `Pillow` |
| **`send_email.py`** | Sends automated emails using Gmail SMTP. | `smtplib`, `ssl` |
| **`clean_csv.py`** | Removes duplicates and fills missing values in a CSV file. | `pandas` |
| **`get_weather.py`** | Fetches current weather for a city using OpenWeatherMap API. | `requests` |
| **`merge_pdfs.py`** | Combines all PDF files in a folder into a single document. | `PyPDF2` |
| **`clip_shortener.py`** | Runs in the background, detects URLs in clipboard, and shortens them. | `pyperclip`, `requests` |
| **`backup_folder.py`** | Zips a specific folder with a timestamped filename for backup. | `shutil` |
| **`extract_pdf_pages.py`**| Extracts specific pages from a PDF and saves them as a new file. | `PyPDF2` |

---

## ⚙️ Setup & Installation

1.  **Clone the repository** (or download the files).
2.  **Install Dependencies:**
    All required libraries are listed in `requirements.txt`. Install them all at once:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage Guide

**Important:** Before running any script, open the file in your code editor (like VS Code) and look for the **CONFIGURATION** section at the top. You usually need to update paths, API keys, or email credentials.

### 1. File Organizer
* **Config:** Set `SOURCE_FOLDER` to the directory you want to clean.
* **Run:** `python organize_files.py`

### 2. Web Scraper
* **Config:** Target URL is set to a test sandbox. No config needed.
* **Run:** `python scrape_quotes.py`

### 3. Uptime Checker
* **Config:** Add URLs to `WEBSITES_TO_CHECK`.
* **Run:** `python check_uptime.py` (Press `Ctrl+C` to stop).

### 4. Bulk Image Resizer
* **Config:** Set `SOURCE_FOLDER`, `OUTPUT_FOLDER`, and `MAX_SIZE`.
* **Run:** `python resize_images.py`

### 5. Email Sender
* **Config:** Update `SENDER_EMAIL`, `SENDER_PASSWORD` (use an **App Password**), and `RECEIVER_EMAIL`.
* **Run:** `python send_email.py`

### 6. CSV Cleaner
* **Config:** Ensure `input_data.csv` exists in the folder (or update filename).
* **Run:** `python clean_csv.py`

### 7. Weather Notifier
* **Config:** Get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and paste it into `API_KEY`. Set your `CITY`.
* **Run:** `python get_weather.py`

### 8. PDF Merger
* **Config:** Place PDF files in the same folder as the script.
* **Run:** `python merge_pdfs.py`

### 9. URL Shortener
* **Config:** None required (uses TinyURL API).
* **Run:** `python clip_shortener.py` (Runs in background. Copy a URL to test. Press `Ctrl+C` to stop).

### 10. Folder Backup
* **Config:** Set `SOURCE_FOLDER` (to back up) and `DESTINATION_FOLDER` (where to save).
* **Run:** `python backup_folder.py`

### 11. PDF Page Extractor
* **Config:** Set `SOURCE_PDF` and list the page numbers in `PAGES_TO_EXTRACT`.
* **Run:** `python extract_pdf_pages.py`

---

## ⚠️ Security Note

* **API Keys:** Never commit your real API keys or email passwords to a public GitHub repository.
* **Email:** For the email script, use a Google **App Password**, not your main account password.

---

## 📝 License
This project is free to use for educational and personal automation purposes.
