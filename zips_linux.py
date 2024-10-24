import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# Change root_dir to a suitable path in your Linux environment
root_dir = Path("/home/pirched/Downloads")
destination_dir = Path("/home/pirched/Downloads")
destination_dir.mkdir(parents=True, exist_ok=True)

class ZipHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.zip', '.rar', '.7z', '.tar', '.gz')):
            path = Path(event.src_path)
            time.sleep(1)
            self.extract_zip(path)

    def extract_zip(self, path):
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                print(f"Attempting to extract {path.name} (Attempt {attempt + 1}/{max_attempts})")
                
                final_path = destination_dir / path.stem
                final_path.mkdir(parents=True, exist_ok=True)
                
                # Use unzip for .zip files; adjust commands for other formats as needed
                cmd = ["unzip", "-o", str(path), "-d", str(final_path)]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        print(output.strip(), end='\r')
                
                rc = process.poll()
                if rc != 0:
                    raise subprocess.CalledProcessError(rc, cmd)

                print(f"Extracted {path.name} to {final_path}")
                return
            
            except subprocess.CalledProcessError as e:
                print(f"Error extracting {path.name}: {e}")
                time.sleep(2 ** attempt)
            except Exception as e:
                print(f"Unexpected error extracting {path.name}: {e}")
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
