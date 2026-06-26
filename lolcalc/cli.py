import argparse
from colorama import Fore, Style
from .safe_math import safe_eval
from importlib.metadata import version, PackageNotFoundError

def get_version():
    try:
        return version("lolcalc")
    except PackageNotFoundError:
        return "unknown"

def main():
    parser = argparse.ArgumentParser(description="LolCalc CLI")
    parser.add_argument("expression", nargs="?", help="Math expression to evaluate")
    parser.add_argument("--version", action="store_true", help="Show version")

    args = parser.parse_args()

    if args.version:
        print(Fore.YELLOW + f"LolCalc version: {get_version()}" + Style.RESET_ALL) 
        return

    if args.expression:
        try:
            result = safe_eval(args.expression)
            print(Fore.GREEN + f"Result: {result}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        return

    # Interactive mode
    print(Fore.CYAN + f"LolCalc Version: {get_version()}" + Style.RESET_ALL)
    print(Fore.GREEN + "Type 'exit' or 'quit' to leave." + Style.RESET_ALL)
    print(Fore.MAGENTA + "Type 'help' or '--help' for instructions." + Style.RESET_ALL)
    print(Fore.YELLOW)
    while True:
        expr = input("> ")
        if expr.lower() in ("exit", "quit"):
            break
        elif expr.lower() in ("version", "--version"):
            print(Fore.YELLOW + f"LolCalc version: {get_version()}" + Style.RESET_ALL)
            print(Fore.YELLOW)
            continue
        elif expr.lower() in ("help", "--help"):
            print(Fore.MAGENTA + "Enter a math expression to evaluate it." + Style.RESET_ALL)
            print(Fore.MAGENTA + "Supported operators: +, -, *, /, **, %, unary -." + Style.RESET_ALL)
            print(Fore.MAGENTA + "Type 'exit' or 'quit' to leave." + Style.RESET_ALL)
            print(Fore.YELLOW)
            continue
        try:
            print(Fore.GREEN + str(safe_eval(expr)) + Style.RESET_ALL)
            print(Fore.YELLOW, end="")
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
