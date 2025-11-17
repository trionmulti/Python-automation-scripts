import os
import shutil
import datetime
import pathlib

# --- CONFIGURATION ---

# 1. The full path to the folder you want to back up.
#    (Use raw strings (r"...") for Windows paths)
SOURCE_FOLDER = r"C:\Users\YourName\Documents\MyImportantProject"

# 2. The full path to the folder where you want backups to be saved.
#    (This folder will be created if it doesn't exist)
DESTINATION_FOLDER = r"C:\Users\YourName\Desktop\Backups"

# 3. A prefix for the backup file's name.
FILENAME_PREFIX = "MyImportantProject_Backup"

# ---------------------


def main():
    """
    Finds, zips, and saves the source folder to the destination folder.
    """
    print("--- Starting Backup Script ---")
    
    # 1. Setup paths using pathlib for robust path handling
    source_path = pathlib.Path(SOURCE_FOLDER)
    dest_path = pathlib.Path(DESTINATION_FOLDER)
    
    # 2. Check if the source folder exists
    if not source_path.exists():
        print(f"Error: Source folder not found at {source_path}")
        return

    # 3. Create the destination folder if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # 4. Generate the timestamped filename
    #    Format: YYYY-MM-DD_HH-MM-SS
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    #    Filename: e.g., "MyProject_Backup_2025-11-16_23-55-00"
    #    (The .zip extension is added by the 'make_archive' function)
    zip_filename_base = f"{FILENAME_PREFIX}_{timestamp}"
    
    #    Full path for the new archive, without the extension
    archive_path_base = dest_path / zip_filename_base
    
    print(f"Backing up: {source_path}")
    print(f"Saving to:  {dest_path}")
    print(f"Creating archive: {zip_filename_base}.zip")

    try:
        # 5. Create the ZIP archive
        #    shutil.make_archive(base_name, format, root_dir)
        #    'base_name': The full path and name for the output file (minus extension)
        #    'format': 'zip' (or 'tar', 'gztar', etc.)
        #    'root_dir': The folder to compress
        
        shutil.make_archive(
            base_name=archive_path_base,
            format="zip",
            root_dir=source_path
        )
        
        print("\n--- Backup Complete! ---")
        print(f"Successfully created: {zip_filename_base}.zip")

    except Exception as e:
        print(f"\nAn error occurred during archiving: {e}")

if __name__ == "__main__":
    main()
