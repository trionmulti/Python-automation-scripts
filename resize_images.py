import os
from PIL import Image
import pathlib

SOURCE_FOLDER = r"C:\Users\YourName\Pictures\Originals"
OUTPUT_FOLDER = r"C:\Users\YourName\Pictures\Resized"
MAX_SIZE = (800, 800)
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

def resize_images():
    print(f"Resizing images from: {SOURCE_FOLDER}")
    source_path = pathlib.Path(SOURCE_FOLDER)
    output_path = pathlib.Path(OUTPUT_FOLDER)
    output_path.mkdir(parents=True, exist_ok=True)
    
    if not source_path.exists():
        print("Error: Source folder not found.")
        return

    for item in source_path.iterdir():
        if item.is_file() and item.suffix.lower() in IMAGE_EXTENSIONS:
            try:
                img = Image.open(item)
                original_format = img.format 
                img.thumbnail(MAX_SIZE)
                save_path = output_path / item.name
                
                if original_format == 'PNG':
                     img.save(save_path, format='PNG')
                else:
                    if img.mode in ("RGBA", "P"): img = img.convert("RGB")
                    img.save(save_path, format='JPEG', quality=85)
                print(f"Resized: {item.name}")
            except Exception as e:
                print(f"Error processing {item.name}: {e}")

if __name__ == "__main__":
    resize_images()
