import time
import os
from pathlib import Path
import zipfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

root_dir = Path("D:\\Compressed")
destination_dir = Path("D:\\Video")
destination_dir.mkdir(parents=True, exist_ok=True)

class ZipHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.zip'):
            path = Path(event.src_path)
            time.sleep(1)
            self.extract_zip(path)

    def extract_zip(self, path):
        max_attempts=3
        for attempt in range(max_attempts):
            try:
                print(f"Attempting to extract {path.name} (Attempt {attempt + 1}/{max_attempts})")
                with zipfile.ZipFile(path, 'r') as zf:
                    final_path = destination_dir / path.stem
                    final_path.mkdir(parents=True, exist_ok=True)
                    zf.extractall(path=final_path)
                print(f"Extracted {path.name} to {final_path}")
                return
            except PermissionError:
                print(f"Permission Denied for {path.name}. Waiting before retry...")
                time.sleep(2**attempt)
            except zipfile.BadZipFile:
                print(f"{path.name} is not a valid zip file. Skipping.")
                return
            except Exception as e:
                print(f"Error extracting {path.name}: {e}")
                time.sleep(1)
        print(f"Failed to extract {path.name} after {max_attempts} attempts.")

if __name__ == "__main__":
    event_handler = ZipHandler()
    observer = Observer()
    observer.schedule(event_handler, str(root_dir), recursive=False)
    observer.start()

    try:
        print(f"Watching {root_dir} for new zip files. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()