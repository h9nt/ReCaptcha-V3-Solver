from requests       import get, Session
from colorama       import init, Fore, Style
from os             import system
from time           import sleep
from rich.console   import Console
from rich.align     import Align
import shutil
import os

init(autoreset=True)
system("cls" if os.name == "nt" else "clear")


class Deadline:
    def __init__(self, output_path: str = "alive.txt") -> None:
        self.url = "http://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all&page=1&maxtime=3000&logformat=json"
        self.proxies = []
        self.valid = 0
        self.dead = 0
        self.session = Session()
        self.output_path = output_path
        self.console = Console()

    def scrape_proxies(self) -> None:
        try:
            response = self.session.get(self.url, timeout=10)
            response.raise_for_status()
            self.proxies = response.text.strip().split("\n")
            with open("proxies.txt", "w") as file:
                file.write("\n".join(self.proxies))

            print(
                f"{Fore.GREEN}Saved {len(self.proxies)} proxies to proxies.txt{Style.RESET_ALL}"
            )
        except Exception as e:
            print(f"Error fetching proxies: {str(e)}")

    def load_proxy(self, filename: str) -> None:
        if not os.path.isfile(filename):
            print(f"{Fore.YELLOW}Proxy file not found: {filename}{Style.RESET_ALL}")
            return

        with open(filename, "r") as file:
            self.proxies = [line.strip() for line in file if line.strip()]
        if not self.proxies:
            print(f"{Fore.YELLOW}No proxies found in {filename}{Style.RESET_ALL}")

    def check(self, proxy) -> None:
        try:
            response = self.session.get(
                "http://www.google.com",
                proxies={"http": proxy, "https": proxy},
                timeout=5,
            )
            response.raise_for_status()
        except Exception:
            self.dead += 1
        else:
            self.valid += 1
            with open(self.output_path, "a") as output:
                output.write(f"{proxy}\n")

    def display(self) -> None:
        system("cls" if os.name == "nt" else "clear")
        terminal_width = shutil.get_terminal_size().columns
        display_text = f"[!] Alive - [{self.valid}] | Dead - [{self.dead}]"
        centered_text = display_text.center(terminal_width)
        self.console.print(Align.center(centered_text), style="bold green")

    def start(self, threads: int) -> None:
        if not self.proxies:
            print(f"{Fore.YELLOW}No Proxys loaded, trya again!{Style.RESET_ALL}")
            return
            # self.scrape_proxies()

        print(
            f"{Fore.CYAN} [!] Starting proxy checker with {threads} threads...{Style.RESET_ALL}"
        )

        for _ in range(min(threads, len(self.proxies))):
            proxy = self.proxies.pop(0)
            self.check(proxy)
            self.display()
            sleep(1)

        print(
            f"\n{Fore.CYAN}Saved valid proxies to {self.output_path}{Style.RESET_ALL}"
        )


if __name__ == "__main__":
    checker = Deadline()
    while True:
        print(
            f"\n{Fore.YELLOW}[1]{Style.RESET_ALL} Scrape and save proxies to proxies.txt"
        )
        print(f"{Fore.YELLOW}[2]{Style.RESET_ALL} Check proxies from a file")
        print(f"{Fore.YELLOW}[3]{Style.RESET_ALL} Exit")

        choice = input(f"\n{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")

        if choice == "1":
            checker.scrape_proxies()
        elif choice == "2":
            file_name = input(
                f"{Fore.CYAN}Enter the proxy file to check: {Style.RESET_ALL}"
            )
            checker.load_proxy(file_name)
            checker.start(threads=10000)
        elif choice == "3":
            print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
            break
        else:
            print(
                f"{Fore.RED}Invalid choice! Please enter 1, 2, or 3.{Style.RESET_ALL}"
            )


class ProxyScrape:
    "Not recommended"
    def __init__(self, output_path=None) -> None:
        self.output_path = output_path or "proxies.txt"
        self.proxies = []
        self.url = "https://advanced.name/freeproxy/67bb70b609b6a"  # https://advanced.name/freeproxy
        self.sleep = 2

    def _get_proxies(self) -> None:
        try:
            response = get(
                self.url,
                headers={
                    "Connection": "keep-alive",
                    "Host": "advanced.name",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                },
            )
        except Exception as e:
            print(f"{Fore.RED}Error!: {str(e)}{Fore.RESET}")
            return

        proxies = response.text
        for proxy in proxies.splitlines()[:-1]:
            self.proxies.append(proxy)
            with open(self.output_path, "a") as output:
                output.write(f"{proxy}\n")
        input(
            Style.BRIGHT + "[!] Saved Proxys to {}".format(self.output_path),
            flush=True,
            end="\r",
        )
        sleep(self.sleep)


# Made with <3 by @Yilad on Telegram.
