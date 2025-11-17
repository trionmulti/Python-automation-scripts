import os
from PyPDF2 import PdfReader, PdfWriter

SOURCE_PDF = "My_Large_Document.pdf"
PAGES = [1, 2, 5] # 1-based index
OUTPUT = "Extracted_Pages.pdf"

def main():
    if not os.path.exists(SOURCE_PDF): return print("PDF not found")
    reader = PdfReader(SOURCE_PDF)
    writer = PdfWriter()
    
    for p in PAGES:
        if 0 <= p-1 < len(reader.pages):
            writer.add_page(reader.pages[p-1])
            print(f"Added page {p}")
            
    with open(OUTPUT, "wb") as f: writer.write(f)
    print(f"Saved to {OUTPUT}")

if __name__ == "__main__":
    main()
