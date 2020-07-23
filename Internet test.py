import urllib
import time
from urllib.request import urlopen
while True:
    def is_internet():
        """ internet function"""
        print(time.ctime())
        try:
            urlopen("https://www.google.com/", timeout=1)
            return 1
        except:
            urllib.error.URLError
            print("Error")
            return 0
    if is_internet():
        print("Internet connection active")
    else:
        print("Internet connection not active")
    x=(int(input("Press 2 times '0' to quit the program or press 1\nto repeat the test")))
    if x==00:
        break
    if x !=00:
        continue
    # Time must be added
input()
