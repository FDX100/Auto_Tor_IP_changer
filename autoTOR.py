# -*- coding: utf-8 -*-

import os
import subprocess
import time

import requests

from utils import OS, detectOS, printLogo

DEFAULT_CONNECTION = "127.0.0.1:9050"

DEFAULT_PROXIES = {
    "http": f"socks5://{DEFAULT_CONNECTION}",
    "https": f"socks5://{DEFAULT_CONNECTION}",
}


def init():
    os_type = detectOS()

    if os_type == OS.UNKNOWN:
        print("Unsupported operating system")
        return

    if os_type == OS.WINDOWS:
        print("Please make sure: python, pip, requests, tor are installed")
        try:
            subprocess.check_output("pip --version", shell=True)
            print("[!] pip is installed successfully")
        except subprocess.CalledProcessError:
            print("[+] pip is not installed. Please install it manually.")
            return

        try:
            __import__("requests")
            print("[!] python requests is installed")
        except ImportError:
            print("[+] python requests is not installed")
            os.system("pip install requests")
            os.system("pip install requests[socks]")
            print("[!] python requests is installed successfully")

        try:
            check_tor = subprocess.check_output("where tor", shell=True)
            print("[!] tor is installed successfully")
        except subprocess.CalledProcessError:
            print("[+] tor is not installed! Please install it manually.")
            return
    else:  # Assuming Linux or Mac
        print("Please make sure: python3, pip3, requests, tor are installed")
        try:
            check_pip3 = subprocess.check_output("dpkg -s python3-pip", shell=True)
            if str("install ok installed") in str(check_pip3):
                pass
        except subprocess.CalledProcessError:
            print("[+] pip3 not installed")
            subprocess.check_output("sudo apt update", shell=True)
            subprocess.check_output("sudo apt install python3-pip -y", shell=True)
            print("[!] pip3 installed successfully")

        try:
            __import__("requests")
            print("[!] python3 requests is installed")
        except ImportError:
            print("[+] python3 requests is not installed")
            os.system("pip3 install requests")
            os.system("pip3 install requests[socks]")
            print("[!] python3 requests is installed successfully")

        try:
            subprocess.check_output("which tor", shell=True)
        except subprocess.CalledProcessError:
            print("[+] tor is not installed!")
            subprocess.check_output("sudo apt update", shell=True)
            subprocess.check_output("sudo apt install tor -y", shell=True)
            print("[!] tor is installed successfully")
        os.system("clear")


def ma_ip():
    url = "https://www.myexternalip.com/raw"
    get_ip = requests.get(url, proxies=DEFAULT_PROXIES)
    return get_ip.text


def __run_command(win_command: str, linux_command: str):
    if detectOS() == OS.WINDOWS:
        os.system(win_command)
    else:
        os.system(linux_command)


def change():
    __run_command("tor.exe -service reload", "service tor reload")
    print("[+] Your IP has been changed to: " + str(ma_ip()))


def start():
    __run_command("tor.exe", "service tor start")


if __name__ == "__main__":
    init()
    printLogo()

    start()

    time.sleep(3)
    print(f"\033[1;32;40m Change your SOCKETS to {DEFAULT_CONNECTION}\n")
    start()
    try:
        x = int(input("[+] Time to change IP in seconds [default=60] >> "))
        limit = int(
            input(
                "[+] how many times do you want to change your IP [default=1000]? For infinite IP change type [0] >> "
            )
        )
    except ValueError:
        x = 60
        limit = 1000
        print("[!] Invalid input. Using default values.")

    if limit == 0:
        while True:
            try:
                time.sleep(x)
                change()
            except KeyboardInterrupt:
                print("\nAuto TOR is closed.")
                quit()
    else:
        for i in range(limit):
            time.sleep(x)
            change()
