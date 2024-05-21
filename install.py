import os
import shutil

from utils import detectOS, OS

if detectOS() != OS.LINUX:
    print("This script is only for Linux")
    exit()

choice = str(input("[+] to install press (Y) to uninstall press (N) >> "))
run = os.system
if choice.lower() in ("y", "yes"):
    run("chmod 777 autoTOR.py")
    os.mkdir("/usr/share/aut")
    shutil.copy("utils.py", "/usr/share/aut/utils.py")
    shutil.copy("autoTOR.py", "/usr/share/aut/autoTOR.py")

    cmnd = '#! /bin/sh \n exec python3 /usr/share/aut/autoTOR.py "$@"'
    with open("/usr/bin/aut", "w") as file:
        file.write(cmnd)
    run("chmod +x /usr/bin/aut")
    print(
        """\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal """
    )
elif choice.lower() in ("n", "no"):
    shutil.rmtree("/usr/share/aut")
    os.remove("/usr/bin/aut")
    print("[!] now Auto Tor Ip changer has been removed successfully")
else:
    print("[!] wrong choice")
