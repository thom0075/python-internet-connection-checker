#!python3
import requests
import time

log_file = open("logfile.txt", "w")


def generateLog(ctime1, request_obj):
    log_file.write(ctime1 + "\t")
    log_file.write("Status code: " + str(request_obj.status_code))
    log_file.write("\n")


def is_internet():
    """Internet function"""
    print(time.ctime())
    current_time = time.ctime()
    try:
        r = requests.get("https://www.google.com/")  # sends requests to google.com
        if r.status_code == 200:  # if ok, prints msg
            print("Connection established successfully!")
        else:  # if not ok, prints msg
            print("Error, try again")
            # generateLog("logfile", current    _time, r)
    except ConnectionError:  # if this error is enountered, it will print this message
        print(f"No internet connection, time: {time.ctime()}")
    finally:
        print("Generating log file...")
        # time.sleep(0.25)
        generateLog(current_time, r)  # calls the generateLog function
        print("Exiting the program...")


t = 0
while t < 30:
    try:
        is_internet()
        # time.sleep(10)
    except KeyboardInterrupt:
        print("Keyboard Interrupt error ")
        break
    finally:
        t += 1
log_file.close()
input()
