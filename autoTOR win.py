import time
import os
import subprocess
import sys
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def check_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_pip():
    print('[+] pip is not installed')
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print('[!] pip installed successfully')
    except subprocess.CalledProcessError:
        print('[!] Failed to install pip. Please install it manually.')
        sys.exit(1)

def install_requests():
    print('[+] python requests is not installed')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests[socks]"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('[!] python requests is installed ')

def check_tor():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Tor", 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
        winreg.CloseKey(key)
        return True
    except WindowsError:
        return False

def ma_ip():
    url = 'https://www.myexternalip.com/raw'
    get_ip = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    subprocess.run(["net", "stop", "tor"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["net", "start", "tor"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'[+] Your IP has been Changed to: {ma_ip()}')

if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrator privileges. Requesting elevation...")
        run_as_admin()
        sys.exit()

    if not check_pip():
        install_pip()

    try:
        import requests
    except ImportError:
        install_requests()
        import requests

    if not check_tor():
        print('[+] Tor is not installed!')
        print('Please download and install Tor Browser from https://www.torproject.org/')
        input("Press Enter to exit...")
        sys.exit(1)

    os.system('cls')  # Clear the console

    # ASCII Art and introduction
    print('''\033[1;32;40m \n
                    _          _______
         /\        | |        |__   __|
        /  \  _   _| |_ ___      | | ___  _ __
       / /\ \| | | | __/ _ \     | |/ _ \| '__|
      / ____ \ |_| | || (_) |    | | (_) | |
     /_/    \_\__,_|\__\___/     |_|\___/|_|
                    V 2.1 (Windows Edition)
    from mrFD, adapted for Windows
    ''')
    print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

    subprocess.run(["net", "start", "tor"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(3)
    print("\033[1;32;40m change your SOCKS proxy to 127.0.0.1:9050 \n")

    x = input("[+] time to change IP in Sec [type=60] >> ")
    lin = input("[+] how many times do you want to change your IP [type=1000] for infinite IP changes type [0] >> ")

    try:
        if int(lin) == 0:
            while True:
                try:
                    time.sleep(int(x))
                    change()
                except KeyboardInterrupt:
                    print('\nauto tor is closed ')
                    break
        else:
            for i in range(int(lin)):
                time.sleep(int(x))
                change()
    except ValueError:
        print("Invalid input. Please enter a number.")

    print("Auto Tor IP Changer has finished. Press Enter to exit...")
    input()