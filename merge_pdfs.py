import os
import sys
from PyPDF2 import PdfMerger

# --- CONFIGURATION ---

# 1. The name of your final, combined PDF file.
OUTPUT_FILENAME = "Merged_File.pdf"

# 2. The folder to scan. We use "." which means "the current folder
#    (the same folder where this script is saved).
SOURCE_FOLDER = "." 
# ---------------------


def main():
    """
    Finds all PDFs in the current directory, sorts them,
    and merges them into a single PDF.
    """
    print("--- Starting PDF Merger ---")
    
    # 1. Create a PdfMerger object
    merger = PdfMerger()
    
    # 2. Find all PDF files in the source folder
    pdf_files = []
    for item in os.listdir(SOURCE_FOLDER):
        # We check for:
        # 1. It is a file (not a folder)
        # 2. It ends with .pdf (case-insensitive)
        # 3. It is NOT our output file (to avoid merging itself)
        if (os.path.isfile(item) and 
            item.lower().endswith(".pdf") and 
            item != OUTPUT_FILENAME):
            
            pdf_files.append(item)
            
    # 3. Sort the files alphabetically
    #    This is crucial for ensuring the correct order (e.g., page1, page2)
    pdf_files.sort()

    if not pdf_files:
        print(f"Error: No PDF files found to merge in this directory.")
        print("Please add some PDFs and try again.")
        return

    print(f"Found {len(pdf_files)} PDFs. Merging in this order:")
    for i, pdf in enumerate(pdf_files):
        print(f"  {i+1}. {pdf}")
        
    try:
        # 4. Loop through sorted files and append them to the merger
        for pdf in pdf_files:
            merger.append(pdf)
        
        # 5. Write the merged PDF to the output file
        merger.write(OUTPUT_FILENAME)
        
        # 6. Close the merger object
        merger.close()
        
        print(f"\nSuccess! All PDFs merged into: {OUTPUT_FILENAME}")

    except Exception as e:
        print(f"\nAn error occurred during merging: {e}")
        merger.close()

if __name__ == "__main__":
    main()
