from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

def log_info(message):
    print(f"{Fore.CYAN}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{Style.RESET_ALL} {Fore.GREEN}{message}{Style.RESET_ALL}")

def log_error(message):
    print(f"{Fore.CYAN}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{Style.RESET_ALL} {Fore.RED}{message}{Style.RESET_ALL}")