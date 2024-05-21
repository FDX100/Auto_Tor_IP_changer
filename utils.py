import sys
from enum import Enum
from functools import cache


class OS(Enum):
    WINDOWS = "windows"
    MAC = "mac"
    LINUX = "linux"
    UNKNOWN = "unknown"


@cache
def detectOS() -> OS:
    if sys.platform.startswith("win"):
        return OS.WINDOWS
    elif sys.platform.startswith("darwin"):
        return OS.MAC
    elif sys.platform.startswith("linux"):
        return OS.LINUX
    else:
        return OS.UNKNOWN


def printLogo():
    print("""\033[1;32;40m \n
                        _          _______
             /\        | |        |__   __|
            /  \  _   _| |_ ___      | | ___  _ __
           / /\ \| | | | __/ _ \     | |/ _ \| '__|
          / ____ \ |_| | || (_) |    | | (_) | |
         /_/    \_\__,_|\__\___/     |_|\___/|_|
                        V 2.1
        from mrFD
        """)
    print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")
