import os
import shutil
from colorama import init, Fore, Style
import tkinter as tk
from tkinter import filedialog

init(autoreset=True)


# Backuper
def backup_user_conf():
    user_conf = os.path.expandvars(r"%APPDATA%\AnyDesk\user.conf")
    backup_conf = os.path.expanduser("~/Desktop/user.conf.backup")

    if os.path.exists(user_conf):
        try:
            shutil.copy(user_conf, backup_conf)
            print(Style.BRIGHT + Fore.GREEN + f"Backup of user.conf created at: {backup_conf}")
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + f"An error occurred while creating the backup: {e}")
    else:
        print(Style.BRIGHT + Fore.RED + "user.conf file not found. Cannot create backup.")


# Restorer from any directory or def directory
def restore_user_conf():
    user_conf = os.path.expandvars(r"%APPDATA%\AnyDesk\user.conf")

    while True:
        print(Style.BRIGHT + Fore.CYAN + "\nWhere do you want to restore the user.conf file from?")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "1. From default backup (Desktop/user.conf.backup)")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "2. Select backup file manually")

        choice = input(Style.BRIGHT + Fore.CYAN + "Enter your choice (1 or 2): ").strip()

        if choice == '1':
            backup_conf = os.path.expanduser("~/Desktop/user.conf.backup")
            if os.path.exists(backup_conf):
                try:
                    print(Style.BRIGHT + Fore.GREEN + f"Found backup file at {backup_conf}. Restoring...")
                    os.makedirs(os.path.dirname(user_conf), exist_ok=True)
                    shutil.copy(backup_conf, user_conf)
                    print(Style.BRIGHT + Fore.GREEN + "File successfully restored!")
                    return
                except Exception as e:
                    print(Style.BRIGHT + Fore.RED + f"An error occurred while restoring: {e}")
                    return
            else:
                print(Style.BRIGHT + Fore.RED + "Backup file not found on the Desktop.")

        elif choice == '2':
            print(Style.BRIGHT + Fore.CYAN + "Please select the backup file location.")
            root = tk.Tk()
            root.attributes('-topmost', True)
            root.withdraw()
            selected_file = filedialog.askopenfilename(
                title="Select Backup File",
                filetypes=[("Backup files", "*.backup"), ("All files", "*.*")]
            )

            if selected_file:
                try:
                    print(Style.BRIGHT + Fore.GREEN + f"Selected backup file: {selected_file}")
                    os.makedirs(os.path.dirname(user_conf), exist_ok=True)
                    shutil.copy(selected_file, user_conf)
                    print(Style.BRIGHT + Fore.GREEN + "File successfully restored!")
                    return
                except Exception as e:
                    print(Style.BRIGHT + Fore.RED + f"An error occurred while restoring: {e}")
                    return
            else:
                print(Style.BRIGHT + Fore.RED + "No file selected. Please try again or skip.")

        else:
            print(Style.BRIGHT + Fore.RED + "Invalid choice. Please select again.")


# Main menu
if __name__ == "__main__":
    while True:
        print(Style.BRIGHT + Fore.CYAN + "\nSelect an action:")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "1. Backup user.conf")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "2. Restore user.conf from backup")
        print(Style.BRIGHT + Fore.LIGHTRED_EX + "3. Exit")

        choice = input(Style.BRIGHT + Fore.CYAN + "Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            print(Style.BRIGHT + Fore.GREEN + "Creating a backup of user.conf...")
            backup_user_conf()
        elif choice == '2':
            print(Style.BRIGHT + Fore.GREEN + "Restoring user.conf from backup...")
            restore_user_conf()
        elif choice == '3':
            print(Style.BRIGHT + Fore.GREEN + "Exiting the program.")
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid choice. Please try again.")
