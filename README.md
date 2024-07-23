# zipfile-automation

Automates the windows experience when you want to unzip files as soon as they are downloaded

## Table of Contents
- Disclaimer
- Requirements
- Installation

## Disclaimer
You might have to change some parts of the code to suite your device.
- root_dir is where your compressed archives are downloaded into.
- destination_dir is where you would want them.
  
Note that the Drive Letter might be different in your device.

Also check where your 7zip.exe is located in your device. Normally it is in:
```
C:\Program Files\7-zip\7z.exe
```

## Requirements:
have the latest of each!
- Python
- 7zip.exe
- Administrator rights

## Installation
Python Libraries
```python
pip install watchdog
pip install pyinstaller
```

If you want to run the script as an .exe file.
```python
pyinstaller --onefile --noconsole --icon=zipper.ico zips.py
```

If on Windows, you can use Task Scheduler to run the program every time you log in or startup your computer.
