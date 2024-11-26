import os
from colorama import init, Fore, Style

init(autoreset=True)

# Removing service.conf
def IDchanger():
    service_conf_path = os.path.expandvars(r"%ALLUSERSPROFILE%\AnyDesk\service.conf")

    if os.path.exists(service_conf_path):
        try:
            os.remove(service_conf_path)
            print(Style.BRIGHT + Fore.GREEN + f"File '{service_conf_path}' has been successfully deleted.")
        except PermissionError:
            print(Style.BRIGHT + Fore.RED + f"Error: Insufficient permissions to delete the file '{service_conf_path}'. Please run the script as administrator.")
        except OSError as e:
            print(Style.BRIGHT + Fore.RED + f"Error while deleting the file: {e}")
    else:
        print(Style.BRIGHT + Fore.YELLOW + f"File '{service_conf_path}' does not exist. Nothing to delete.")

