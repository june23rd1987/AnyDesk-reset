import os
import shutil
import subprocess
import time
from colorama import init, Fore
from colorama import Back
from colorama import Style
from id_changer import IDchanger
from backup_restore import restore_user_conf
import random
import pyfiglet
init(autoreset=True)


# Backuping user.conf file
def backup_user_conf_main():
    user_conf = os.path.expandvars(r"%APPDATA%\AnyDesk\user.conf")
    backup_conf = os.path.expanduser("~/Desktop/user.conf.backup")

    if os.path.exists(user_conf):
        if os.path.exists(backup_conf):
            print(Style.BRIGHT + Fore.YELLOW + "Backup file user.conf.backup already exists on the Desktop.")
            choice = input(Style.BRIGHT + Fore.CYAN + "Do you want to overwrite it? (y = overwrite, n = keep existing): ").strip().lower()
            if choice == 'y':
                shutil.copy(user_conf, backup_conf)
                print(Style.BRIGHT + Fore.GREEN + "Backup file overwritten successfully.")
            elif choice == 'n':
                print(Style.BRIGHT + Fore.YELLOW + "Using the existing backup file.")
            else:
                print(Style.BRIGHT + Fore.RED + "Invalid choice. Keeping the existing backup file.")
        else:
            print(Style.BRIGHT + Fore.YELLOW + "Creating a new backup of user.conf...")
            shutil.copy(user_conf, backup_conf)
            print(Style.BRIGHT + Fore.GREEN + "Backup completed successfully.")
    else:
        print(Style.BRIGHT + Fore.YELLOW + "The file user.conf was not found. Skipping the save.")

 # Killing AnyDesk
def Killing_AnyDesk():
    print(Style.BRIGHT + Fore.GREEN + "Closing AnyDesk...")
    try:
        result = subprocess.run(
            ["taskkill", "/IM", "AnyDesk.exe", "/F"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(Style.BRIGHT + Fore.GREEN + "AnyDesk has been closed successfully.")
    except subprocess.CalledProcessError:
        print(Style.BRIGHT + Fore.RED + "Failed to close AnyDesk. It may not be running or you lack permissions.")

# Removing old version of Adesk
def remove_anydesk():
    print(Style.BRIGHT + Fore.YELLOW + "Removing the old version of AnyDesk...")

    choice = input(Style.BRIGHT + Fore.CYAN +
                   "Do you want to remove AnyDesk from the default paths (d) or specify a custom path (c)? (d/c): ").strip().lower()

    if choice == 'd':
        # Standart path
        paths_to_remove = [
            r"C:\ProgramData\AnyDesk",
            os.path.expandvars(r"%APPDATA%\AnyDesk"),
            os.path.expandvars(r"%LOCALAPPDATA%\AnyDesk"),
            r"C:\Program Files (x86)\AnyDesk"
        ]
        for path in paths_to_remove:
            if os.path.exists(path):
                shutil.rmtree(path, ignore_errors=True)
                print(Style.BRIGHT + Fore.YELLOW + f"Deleted: {path}")
            else:
                print(Style.BRIGHT + Fore.YELLOW + f"Folder {path} is already missing.")
    elif choice == 'c':
        # Custom path if user wants
        print(Style.BRIGHT + Fore.CYAN + "Please select the folder you want to remove.")
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        custom_path = filedialog.askdirectory(title="Select AnyDesk Directory")

        if custom_path:
            if os.path.exists(custom_path):
                try:
                    shutil.rmtree(custom_path, ignore_errors=True)
                    print(Style.BRIGHT + Fore.GREEN + f"Deleted: {custom_path}")
                except OSError as e:
                    print(Style.BRIGHT + Fore.RED + f"Failed to delete {custom_path}: {e}")
            else:
                print(Style.BRIGHT + Fore.RED + f"The specified path '{custom_path}' does not exist.")
        else:
            print(Style.BRIGHT + Fore.GREEN + "No folder selected. Skipping AnyDesk removal.")
    else:
        print(Style.BRIGHT + Fore.RED + "Invalid input. Skipping AnyDesk removal.")


# Installing new AnyDesk if user wants
import tkinter as tk
from tkinter import filedialog
import subprocess


def install_anydesk():
    choice = input(Style.BRIGHT + Fore.CYAN + "Do you want to install a new version of AnyDesk? (y = install, n = skip): ").strip().lower()

    if choice == 'y':
        print(Style.BRIGHT + Fore.GREEN + "Please select the AnyDesk installer (.exe file).")
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        installer_path = filedialog.askopenfilename(
            title="Select AnyDesk Installer",
            filetypes=[("Executable files", "*.exe")],
        )

        if installer_path:
            print(f"Selected installer: {installer_path}")
            try:
                print(Style.BRIGHT + Fore.YELLOW + "Running the installer...")
                subprocess.run(installer_path, check=True)
                print(Style.BRIGHT + Fore.GREEN + "Installation completed.")
                restore_user_conf_main()
            except subprocess.CalledProcessError as e:
                print(Style.BRIGHT + Fore.RED + f"Error during installation: {e}")
        else:
            print(Style.BRIGHT + Fore.RED + "No file selected. Installation aborted.")

    elif choice == 'n':
        print(Style.BRIGHT + Fore.GREEN + "Skipping the installation.")

    else:
        print(Style.BRIGHT + Fore.RED + "Invalid choice. Installation skipped.")

# Restoring old user.conf from backup
def restore_user_conf_main():
    backup_conf = os.path.expanduser("~/Desktop/user.conf.backup")
    user_conf = os.path.expandvars(r"%APPDATA%\AnyDesk\user.conf")

    if os.path.exists(backup_conf):
        print(Style.BRIGHT + Fore.GREEN + "Restoring the user.conf file...")
        os.makedirs(os.path.dirname(user_conf), exist_ok=True)
        shutil.copy(backup_conf, user_conf)
    else:
          print(Style.BRIGHT + Fore.RED + "Backup file user.conf not found. Skipping restoration.") # why?

# Running AnyDesk if user wants
def run_anydesk():
    choice = input(Style.BRIGHT + Fore.CYAN + "Do you want to run AnyDesk now? (y = run, n = don't run): ").strip().lower()

    if choice == 'y':
        anydesk_path = r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe"
        if os.path.exists(anydesk_path):
            print(Style.BRIGHT + Fore.GREEN + "Starting AnyDesk...")

            subprocess.Popen([anydesk_path])

            if check_anydesk_running():
                print(Style.BRIGHT + Fore.GREEN + "AnyDesk is running successfully.")
                return
            else:
                print(Style.BRIGHT + Fore.RED + "Failed to start AnyDesk.")
        else:
            print(Style.BRIGHT + Fore.RED + f"AnyDesk not found at {anydesk_path}. Make sure it's installed.")

    elif choice == 'n':
        print(Style.BRIGHT + Fore.GREEN + "Not running AnyDesk.")

    else:
        print(Style.BRIGHT + Fore.RED + "Invalid choice. Skipping AnyDesk launch.")

def check_anydesk_running():
    try:
        result = subprocess.run("tasklist /fi \"imagename eq AnyDesk.exe\"", capture_output=True, text=True)
        if "AnyDesk.exe" in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(Style.BRIGHT + Fore.RED + f"Error checking AnyDesk process: {e}")
        return False

# Starting ID Changer module
def IDchangerQuestion():
    choice = input(Style.BRIGHT + Fore.CYAN + "Change AnyDesk ID? (y = Yes, n = No): ").strip().lower()

    if choice == 'y':
        print(Style.BRIGHT + Fore.GREEN + "Changing ID...")
        IDchanger()
    elif choice == 'n':
        print(Style.BRIGHT + Fore.GREEN + "Skipping ID change.")
    else:
        print(Style.BRIGHT + Fore.RED + "Invalid input. Skipping ID change.")

# Logo
def colorful_text(text):
    color_choices = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
    ]
    result = ""
    for char in text:
        color = random.choice(color_choices)
        result += color + char
    return result

# ASCII logo
anydesk_text = pyfiglet.figlet_format("AnyDesk", font="slant")
reset_text = pyfiglet.figlet_format("reset", font="slant")

def main_cleanup():
    backup_user_conf_main()
    Killing_AnyDesk()
    remove_anydesk()
    restore_user_conf_main()
    install_anydesk()
    IDchangerQuestion()
    run_anydesk()
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "Done, enjoy!")

if __name__ == "__main__":
    while True:
        print(Style.BRIGHT + Fore.RED + anydesk_text); print(Style.BRIGHT + colorful_text(reset_text))
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + "Made by MKultra69")
        print(Fore.LIGHTWHITE_EX + "GitHub: https://github.com/MKultra6969/AnyDesk-reset")
        print(Style.BRIGHT + Fore.CYAN + "\nSelect an action:")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "1. Main cleanup")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "2. Change AnyDesk ID")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "3. Backup/Restore user.conf")
        print(Style.BRIGHT + Fore.LIGHTRED_EX + "4. Exit")

        choice = input(Style.BRIGHT + Fore.CYAN + "Enter your choice (1, 2, 3, or 4): ").strip()

        if choice == '1':
            print(Style.BRIGHT + Fore.GREEN + "Running the Main cleanup tool...")
            main_cleanup()
        elif choice == '2':
            print(Style.BRIGHT + Fore.GREEN + "Running the ID changer tool...")
            Killing_AnyDesk()
            IDchanger()
        elif choice == '3':
            print(Style.BRIGHT + Fore.GREEN + "Running the Backup/Restore tool...")
            restore_user_conf()
            run_anydesk()
        elif choice == '4':
            print(Style.BRIGHT + Fore.GREEN + "Exiting the program.")
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid choice. Please try again.")



# Why? Idk.

# upd 26.11.24 03:17PM Why are you reading this shit, you little motherfucker?
# upd 27.11.24
