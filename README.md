[🇷🇺Русский](https://github.com/MKultra6969/AnyDesk-reset/blob/main/README.ru.md)

# AnyDesk Reset Script

This Python script allows you to reset your AnyDesk installation, including backing up and restoring your configuration, removing the current installation, installing a fresh version, and launching AnyDesk.

# Features

- **Backup the `user.conf` file**  
  Automatically creates a backup of your AnyDesk configuration file (`user.conf`) on your desktop for safekeeping.

- **Remove the old version of AnyDesk**  
  Cleans up AnyDesk installation directories to ensure a fresh start and avoid conflicts with previous installations.

- **Install a new version of AnyDesk**  
  Allows manual installation by selecting the `.exe` installer through an intuitive file dialog.

- **Restore the `user.conf` file**  
  Restores your previous AnyDesk configuration from the backup to retain custom settings.

- **Launch AnyDesk**  
  Provides an option to automatically run AnyDesk after the script completes its tasks.

- **Menu-driven operation**  
  At the start, the script presents a menu for the user to choose between:
  1. Running the main cleanup and reinstallation process.
  2. Running the AnyDesk ID changer function.

- **Change AnyDesk ID**  
  Deletes the `service.conf` file to reset the current AnyDesk ID, enabling a fresh identification setup.


## Requirements
- Python 3.x
- `colorama` library for colored output (you can install it using `pip install colorama`)
- Tkinter for the file dialog (usually comes pre-installed with Python)

## Installation

1. Clone the repository or download the script.
2. Install required dependencies:

   ```bash
   pip install colorama
