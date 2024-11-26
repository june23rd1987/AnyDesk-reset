import os
import shutil
import subprocess
import time
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

# Backuping user.conf file
def backup_user_conf():
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
    print(Style.BRIGHT + Fore.GREEN + "Closing AnyDesk...")
    try:
        subprocess.run(["taskkill", "/IM", "AnyDesk.exe", "/F"], check=True)
        print(Style.BRIGHT + Fore.GREEN + "AnyDesk has been closed successfully.")
    except subprocess.CalledProcessError:
        print(Style.BRIGHT + Fore.RED + "Failed to close AnyDesk. It might not be running.")

# Removing old version of Adesk
def remove_anydesk():
    print(Style.BRIGHT + Fore.YELLOW + "Removing the old version of AnyDesk...")
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
            print(Style.BRIGHT + Fore.YELLOW + f"Folder {path} Already missing..")

# Installing new AnyDesk
import tkinter as tk
from tkinter import filedialog
import subprocess


def install_anydesk():
    choice = input(Style.BRIGHT + Fore.CYAN + "Do you want to install a new version of AnyDesk? (y = install, n = skip): ").strip().lower()

    if choice == 'y':
        print(Style.BRIGHT + Fore.GREEN + "Please select the AnyDesk installer (.exe file).")
        root = tk.Tk()
        root.attributes('-topmost', True)  # Окно всегда сверху
        root.withdraw()  # Скрываем окно, но не удаляем его
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
            except subprocess.CalledProcessError as e:
                print(Style.BRIGHT + Fore.RED + f"Error during installation: {e}")
        else:
            print(Style.BRIGHT + Fore.RED + "No file selected. Installation aborted.")

    elif choice == 'n':
        print(Style.BRIGHT + Fore.GREEN + "Skipping the installation.")

    else:
        print(Style.BRIGHT + Fore.RED + "Invalid choice. Installation skipped.")

# Restoring old user.conf from backup
def restore_user_conf():
    backup_conf = os.path.expanduser("~/Desktop/user.conf.backup")
    user_conf = os.path.expandvars(r"%APPDATA%\AnyDesk\user.conf")

    if os.path.exists(backup_conf):
        print(Style.BRIGHT + Fore.GREEN + "Restoring the user.conf file...")
        os.makedirs(os.path.dirname(user_conf), exist_ok=True)
        shutil.copy(backup_conf, user_conf)
    else:
          print(Style.BRIGHT + Fore.RED + "Backup file user.conf not found. Skipping restoration.") # why?

# Running AnyDesk
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

if __name__ == "__main__":
    backup_user_conf()
    remove_anydesk()
    install_anydesk()
    restore_user_conf()
    run_anydesk()
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "Done, enjoy!")

# Why? Idk.