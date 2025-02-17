# -*- coding: utf-8 -*-
'''
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 3.0
from 2600 Hackers. We disarmed and anonymised your script that kept reporting back home at Aws.
'''

import time

try:
    import requests
    from invoke import task

except Exception:
    print('[+] python3 requests[socks] and py-invoke is not installed')

def changeIp(ctx, seconds):
        try:
            time.sleep(int(seconds))
            ctx.run(f'killall -HUP tor')
        except KeyboardInterrupt:
            break

@task
def rotate(context, seconds=60, rotations=1):
    "Change your IP address every nth seconds for total nth rotations"
    for _ in range(rotations):
        changeIp(ctx,seconds)

@task(default=True)
def daemon(context, seconds=60):
    "Change your IP address every nth seconds"
    while True:
        changeIp(context, seconds)
