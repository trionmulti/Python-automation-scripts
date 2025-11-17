import os
import shutil
import pathlib

# --- CONFIGURATION ---
# 1. Set the folder you want to organize.
#    (Use a raw string (r"...") for Windows paths to avoid issues with backslashes)
#    Examples:
#    Windows: r"C:\Users\YourName\Downloads"
#    Mac/Linux: "/home/YourName/Downloads"
SOURCE_FOLDER = r"C:\Users\YourName\Downloads"


# 2. Define where files should go based on their extension.
#    (Feel free to add/remove categories and extensions)
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
}

# 3. Name for the folder to put all other/uncategorized files.
OTHER_FOLDER = "Other"
# ---------------------

def main():
    """
    Main function to organize files in the source folder.
    """
    print(f"Starting to organize files in: {SOURCE_FOLDER}\n")
    
    # Use pathlib.Path for easier and safer path operations
    source_path = pathlib.Path(SOURCE_FOLDER)
    
    if not source_path.exists():
        print(f"Error: Source folder not found at {SOURCE_FOLDER}")
        return

    # Create a reverse mapping for quick lookup: {".pdf": "Documents", ".jpg": "Images"}
    extension_mapping = {}
    for category, extensions in FILE_CATEGORIES.items():
        for ext in extensions:
            extension_mapping[ext] = category

    # Iterate over all files in the source folder
    # We use .iterdir() which lists all items (files and folders)
    for item in source_path.iterdir():
        
        # Skip items that are directories (folders)
        if item.is_dir():
            continue
        
        # Skip this script itself if it's in the folder
        if item.name == "organize_files.py":
            continue

        # Get the file extension (e.g., ".pdf")
        file_extension = item.suffix.lower()
        
        # Find the matching category
        category_name = extension_mapping.get(file_extension, OTHER_FOLDER)
        
        # Create the destination folder path
        dest_folder = source_path / category_name
        
        # Create the folder if it doesn't exist
        dest_folder.mkdir(exist_ok=True)
        
        # Create the full path for the destination file
        dest_file_path = dest_folder / item.name
        
        # Move the file
        try:
            shutil.move(str(item), str(dest_file_path))
            print(f"Moved: {item.name}  ->  {category_name}")
        except Exception as e:
            print(f"Error moving {item.name}: {e}")

    print("\nOrganization complete!")

if __name__ == "__main__":
    main()
