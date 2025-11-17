import os
import shutil
import pathlib

# --- CONFIGURATION ---
SOURCE_FOLDER = r"C:\Users\YourName\Downloads"

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
}

OTHER_FOLDER = "Other"

def main():
    '''Main function to organize files.'''
    print(f"Starting to organize files in: {SOURCE_FOLDER}")
    source_path = pathlib.Path(SOURCE_FOLDER)
    
    if not source_path.exists():
        print(f"Error: Source folder not found at {SOURCE_FOLDER}")
        return

    extension_mapping = {}
    for category, extensions in FILE_CATEGORIES.items():
        for ext in extensions:
            extension_mapping[ext] = category

    for item in source_path.iterdir():
        if item.is_dir() or item.name == "organize_files.py":
            continue

        file_extension = item.suffix.lower()
        category_name = extension_mapping.get(file_extension, OTHER_FOLDER)
        dest_folder = source_path / category_name
        dest_folder.mkdir(exist_ok=True)
        dest_file_path = dest_folder / item.name
        
        try:
            shutil.move(str(item), str(dest_file_path))
            print(f"Moved: {item.name} -> {category_name}")
        except Exception as e:
            print(f"Error moving {item.name}: {e}")

if __name__ == "__main__":
    main()
