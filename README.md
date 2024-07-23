# zipfile-automation

Automates the windows experience when you want to unzip files as soon as they are downloaded

## Table of Contents
- Requirements

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
