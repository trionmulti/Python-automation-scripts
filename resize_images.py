import os
import sys
from PIL import Image
import pathlib

# --- CONFIGURATION ---

# 1. The folder where your original images are.
#    (Use raw strings (r"...") for Windows paths)
SOURCE_FOLDER = r"C:\Users\YourName\Pictures\Originals"

# 2. The folder where the resized images will be saved.
#    This folder will be created if it doesn't exist.
OUTPUT_FOLDER = r"C:\Users\YourName\Pictures\Resized"

# 3. The maximum size (width, height) for your resized images.
#    The script will maintain the aspect ratio, so the image will
#    fit *within* these dimensions.
MAX_SIZE = (800, 800)  # (width, height) in pixels

# 4. A list of image file types to look for.
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
# ---------------------


def resize_images():
    """
    Finds, resizes, and saves images from the source folder to the output folder.
    """
    print(f"Resizing images from: {SOURCE_FOLDER}")
    print(f"Saving to: {OUTPUT_FOLDER}\n")

    # 1. Setup paths using pathlib for robust path handling
    source_path = pathlib.Path(SOURCE_FOLDER)
    output_path = pathlib.Path(OUTPUT_FOLDER)
    
    # 2. Create the output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 3. Check if the source folder exists
    if not source_path.exists():
        print(f"Error: Source folder not found at {SOURCE_FOLDER}")
        return

    # 4. Loop through all files in the source folder
    files_processed = 0
    files_skipped = 0
    for item in source_path.iterdir():
        
        # Check if it's a file and its extension is in our list
        if item.is_file() and item.suffix.lower() in IMAGE_EXTENSIONS:
            # 5. Open the image
            try:
                img = Image.open(item)
                
                # Keep a copy of the original format (like 'PNG')
                original_format = img.format 
                
                # 6. Resize the image (maintaining aspect ratio)
                #    .thumbnail() modifies the image in-place
                img.thumbnail(MAX_SIZE)
                
                # 7. Determine the new file name and save path
                #    We'll save it with the same name in the output folder.
                #    We need to handle formats like JPEG that can't save transparency.
                save_path = output_path / item.name
                
                # Special handling for PNGs to preserve transparency
                if original_format == 'PNG':
                     img.save(save_path, format='PNG')
                # Other formats (like JPG) can be saved normally
                else:
                    # Convert to RGB if it's a format that needs it (e.g., some GIFs)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    img.save(save_path, format='JPEG', quality=85) # Save as JPEG with 85% quality
                
                print(f"Resized: {item.name}")
                files_processed += 1
                
            except Exception as e:
                print(f"Error processing {item.name}: {e}")
                files_skipped += 1
        else:
            if item.is_file():
                # This just lets you know if files are being skipped
                # print(f"Skipped (not an image): {item.name}")
                files_skipped += 1

    print("\n--- Bulk Resizing Complete ---")
    print(f"Files resized: {files_processed}")
    print(f"Files skipped: {files_skipped}")

if __name__ == "__main__":
    resize_images()
