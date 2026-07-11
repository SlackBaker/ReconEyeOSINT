from colorama import Fore, init

from findncknames.whereisnickname import checknickname
from src.services.victim_info.biography import initialize
from src.services.victim_info.where_is_signed import where_is_signed

init()

def main():
    while True:
        userinput = input(Fore.GREEN + "> ").strip()

        match userinput.lower():
            case "quit" | "exit" | "x":
                break

            case "biography":
                initialize.initialize()

            case "issigned":
                where_is_signed.checknickname()

            case _:
                print(Fore.YELLOW + "Unknown command")

if __name__ == "__main__":
    main()