[🇷🇺Русский](https://github.com/MKultra6969/AnyDesk-reset/blob/main/README.ru.md)

# AnyDesk Reset Tool (A.R.T.)
### ❗❗New version is avalible [MK_AdeskUtils](https://github.com/Project-MKDELTA/MK_ADeskUtils)❗❗
![34cb70a4-da4c-47dd-a433-1b57c945ecf6](https://github.com/user-attachments/assets/1e5b52c6-ad29-43dc-a661-171a96d9af22)




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
- Colorama
- pyfiglet

## Installation

1. `git clone https://github.com/june23rd1987/AnyDesk-reset` - _Clone the repository to any directory_
2. `cd AnyDesk-reset` - _Navigate to the script directory_
3. `pip install -r requirements.txt` - _Install dependencies_
4. `python Adesk_reset.py` - _Run the script_
