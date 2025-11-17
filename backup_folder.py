import shutil
import datetime
import pathlib

SOURCE_FOLDER = r"C:\Users\YourName\Documents\MyProject"
DESTINATION_FOLDER = r"C:\Users\YourName\Desktop\Backups"
PREFIX = "Backup"

def main():
    src = pathlib.Path(SOURCE_FOLDER)
    dst = pathlib.Path(DESTINATION_FOLDER)
    if not src.exists(): return print("Source not found")
    dst.mkdir(parents=True, exist_ok=True)
    
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name = dst / f"{PREFIX}_{ts}"
    
    shutil.make_archive(name, 'zip', src)
    print(f"Backup created: {name}.zip")

if __name__ == "__main__":
    main()
