import os
from PyPDF2 import PdfMerger

OUTPUT_FILENAME = "Merged_File.pdf"
SOURCE_FOLDER = "."

def main():
    print("Merging PDFs...")
    merger = PdfMerger()
    pdf_files = sorted([f for f in os.listdir(SOURCE_FOLDER) if f.lower().endswith(".pdf") and f != OUTPUT_FILENAME])

    if not pdf_files:
        print("No PDFs found.")
        return

    for pdf in pdf_files:
        merger.append(pdf)
        print(f"Added: {pdf}")
        
    merger.write(OUTPUT_FILENAME)
    merger.close()
    print(f"Saved to: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()
