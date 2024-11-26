[🇷🇺Русский](https://github.com/MKultra6969/AnyDesk-reset/blob/main/README.ru.md)

# AnyDesk Reset Script

This Python script allows you to reset your AnyDesk installation, including backing up and restoring your configuration, removing the current installation, installing a fresh version, and launching AnyDesk.

## Features
- **Backup the `user.conf` file**: Saves your AnyDesk configuration file (`user.conf`) to your desktop.
- **Remove the old version of AnyDesk**: Cleans up AnyDesk installation directories to ensure a fresh start.
- **Install a new version of AnyDesk**: Allows you to manually install AnyDesk by selecting the `.exe` installer.
- **Restore the `user.conf` file**: Restores your previous AnyDesk configuration from the backup.
- **Launch AnyDesk**: Optionally run AnyDesk after the script finishes.

## Requirements
- Python 3.x
- `colorama` library for colored output (you can install it using `pip install colorama`)
- Tkinter for the file dialog (usually comes pre-installed with Python)

## Installation

1. Clone the repository or download the script.
2. Install required dependencies:

   ```bash
   pip install colorama
