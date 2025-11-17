import os
from PyPDF2 import PdfReader, PdfWriter

# --- CONFIGURATION ---

# 1. The name of the large PDF you want to split/extract from.
SOURCE_PDF = "My_Large_Document.pdf"

# 2. The specific page numbers you want to extract.
#    (Enter them exactly as they appear in the document footer)
#    Example: [1, 3, 5] will get the 1st, 3rd, and 5th pages.
PAGES_TO_EXTRACT = [1, 2, 5]

# 3. The name of the new file that will contain these pages.
OUTPUT_FILENAME = "Extracted_Pages.pdf"

# ---------------------


def main():
    """
    Extracts specific pages from a PDF and saves them to a new file.
    """
    print(f"--- Extracting pages from: {SOURCE_PDF} ---")

    # Check if source file exists
    if not os.path.exists(SOURCE_PDF):
        print(f"Error: File '{SOURCE_PDF}' not found.")
        return

    try:
        # 1. Open the source PDF
        reader = PdfReader(SOURCE_PDF)
        writer = PdfWriter()
        
        # Get total number of pages to prevent errors
        total_pages = len(reader.pages)
        print(f"Source document has {total_pages} pages.")

        pages_added = 0

        # 2. Loop through the list of requested pages
        for page_num in PAGES_TO_EXTRACT:
            
            # Convert human page number (1-based) to Python index (0-based)
            page_index = page_num - 1
            
            # 3. Check if the page actually exists
            if 0 <= page_index < total_pages:
                # Get the page object
                page = reader.pages[page_index]
                
                # Add it to the writer
                writer.add_page(page)
                
                print(f"  - Added Page {page_num}")
                pages_added += 1
            else:
                print(f"  ! Warning: Page {page_num} is out of range (Skipped).")

        # 4. Save the new PDF
        if pages_added > 0:
            with open(OUTPUT_FILENAME, "wb") as output_file:
                writer.write(output_file)
            print(f"\nSuccess! {pages_added} pages saved to: {OUTPUT_FILENAME}")
        else:
            print("\nNo pages were added. Output file was not created.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
