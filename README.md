# Linux Project Manager (LPM)

Linux Project Manager (LPM) is a Python-based desktop application designed to save and restore desktop setups for different "projects."  
A project setup includes open applications, their window positions, file paths, and URLs, making it easy to switch between different workflows.  

## Features
- Save the current desktop setup:
  - Applications, file paths, and URLs.
  - Window positions and sizes.
- Restore a saved project setup with one click.
- Manage multiple project configurations.

## Requirements
### Operating System
- Linux (Tested on Ubuntu-based distributions)

### Dependencies
- Python 3.8 or later
- Required Python packages:
  - `xdotool` (For managing windows)
  - `pyxdg` (For opening applications)
  - `json` (For configuration management, built-in)

Install the required Python packages:  
```bash
pip install -r requirements.txt
