import time
import os

os.system("clear")

print('''\033[1;32;40m \n

___  __   __        __      __                  __   ___  __      __          ___  __  
 |  /  \ |__)    | |__)    /  ` |__|  /\  |\ | / _` |__  |__)    |__) \ /    |__  |  \ 
 |  \__/ |  \    | |       \__, |  | /~~\ | \| \__> |___ |  \    |__)  |     |    |__/ 
                                                                                       




''')
print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")
print("\033[1;40;31m *if you dont have tor . then you must install tor (sudo apt-get install tor , sudo apt-get install privoxy)\n")
os.system("service tor start")




time.sleep(5)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("time to change Ip in Sec {type=60}")
lin = input("how many time do you want to change your ip {type=1000}")

for i in range(lin):  
      time.sleep(x)
      os.system("service tor reload")
      print("<<<<<<<<<<<<<<<<Your IP has been Changed>>>>>>>>>>>>>>>>>") 
      

