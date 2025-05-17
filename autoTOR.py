# -*- coding: utf-8 -*-
import time
import os
import subprocess
import sys
import socket

TOR_CONTROL_PASSWORD = "your_password_here"  # Put your Tor control password here (plaintext)

def str_to_hex(s):
    return ''.join(f'{ord(c):02X}' for c in s)

def install_python_packages():
    try:
        import requests
        import socks  # from pysocks
    except ImportError:
        print('[+] Required Python packages not found. Installing now...')
        os.system('pip3 install "requests[socks]" pysocks')
        # Try importing again after installation
        try:
            import requests
            import socks
        except ImportError:
            print('[!] Failed to install required Python packages. Please install them manually.')
            sys.exit(1)

install_python_packages()
import requests

def ensure_tor_installed():
    try:
        subprocess.check_output('which tor', shell=True)
    except subprocess.CalledProcessError:
        print('[+] Tor is not installed. Installing...')
        subprocess.call('sudo apt update', shell=True)
        subprocess.call('sudo apt install tor -y', shell=True)
        print('[!] Tor installed successfully.')

def start_tor():
    try:
        subprocess.call('sudo service tor start', shell=True)
    except:
        try:
            subprocess.call('sudo systemctl start tor', shell=True)
        except Exception as e:
            print(f'[!] Could not start Tor service: {e}')

def send_newnym():
    """
    Sends the NEWNYM signal to Tor control port to request a new circuit/IP.
    Requires Tor to be configured with ControlPort 9051 and password authentication.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 9051))
        hex_pass = str_to_hex(TOR_CONTROL_PASSWORD)
        auth_cmd = f'AUTHENTICATE {hex_pass}\r\n'.encode()
        s.send(auth_cmd)
        response = s.recv(1024)
        if b'250' not in response:
            print("[!] Authentication failed with Tor control port")
            s.close()
            return False
        s.send(b'SIGNAL NEWNYM\r\n')
        response = s.recv(1024)
        if b'250' in response:
            print("[+] Successfully sent NEWNYM signal to Tor")
            s.close()
            return True
        else:
            print("[!] Failed to send NEWNYM signal")
        s.close()
    except Exception as e:
        print(f"[!] Error communicating with Tor control port: {e}")
        return False

def get_ip():
    url = 'http://checkip.amazonaws.com'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        return response.text.strip()
    except Exception as e:
        return f'[!] Failed to get IP: {e}'

def change_ip():
    if send_newnym():
        time.sleep(5)  # Wait for the new circuit to be established
        print('[+] Your IP has been changed to:', get_ip())
    else:
        print('[!] Could not change IP via NEWNYM signal.')

def main():
    ensure_tor_installed()
    os.system("clear")

    print('''\033[1;32;40m
                _          _______
     /\\        | |        |__   __|
    /  \\  _   _| |_ ___      | | ___  _ __
   / /\\ \\| | | | __/ _ \\     | |/ _ \\| '__|
  / ____ \\ |_| | || (_) |    | | (_) | |
 /_/    \\_\\__,_|\\__\\___/     |_|\\___/|_|
                V 2.1
from mrFD
''')
    print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

    start_tor()
    time.sleep(3)
    print("\033[1;32;40m Set your SOCKS to 127.0.0.1:9050 \n")

    delay_input = input("[+] Time delay to change IP in seconds [default=60] >> ") or "60"
    count_input = input("[+] How many times to change IP? (Enter 0 or leave blank for infinite) >> ") or "0"

    try:
        delay = int(delay_input)
        count = int(count_input)

        if count == 0:
            print("[*] Starting infinite IP change. Press Ctrl+C to stop.")
            while True:
                time.sleep(delay)
                change_ip()
        else:
            for _ in range(count):
                time.sleep(delay)
                change_ip()

    except ValueError:
        print("[!] Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
