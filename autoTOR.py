# -*- coding: utf-8 -*-

import time
import os
import subprocess

def command_exists(command):
    return subprocess.call(f"command -v {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

# Check for pip3 and install if necessary
try:
    subprocess.check_output('pip3 --version', shell=True)
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('pkg update && pkg install -y python-pip', shell=True)
    print('[!] pip3 installed successfully')

# Check for requests and install if necessary
try:
    import requests
except ImportError:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed')

# Check for tor and install if necessary
if not command_exists('tor'):
    print('[+] tor is not installed!')
    subprocess.check_output('pkg update && pkg install -y tor', shell=True)
    print('[!] tor is installed successfully')

os.system("clear")

def ma_ip():
    url = 'https://www.myexternalip.com/raw'
    get_ip = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("pkill -HUP tor")
    print('[+] Your IP has been Changed to: ' + str(ma_ip()))

print('''\033[1;32;40m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.1
from mrFD
''')
print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

os.system("tor &")

time.sleep(3)
print("\033[1;32;40m change your SOCKS to 127.0.0.1:9050 \n")
x = input("[+] time to change Ip in Sec [type=60] >> ")
lin = input("[+] how many times do you want to change your IP [type=1000] for infinite IP change type [0] >> ")

if int(lin) == 0:
    while True:
        try:
            time.sleep(int(x))
            change()
        except KeyboardInterrupt:
            print('\nauto tor is closed')
            quit()
else:
    for i in range(int(lin)):
        time.sleep(int(x))
        change()
