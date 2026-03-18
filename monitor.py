import requests
import time
from datetime import datetime

URL = "https://google.com"

def check_website():
    try:
        response = requests.get(URL)
        status = "UP" if response.status_code == 200 else "DOWN"
    except:
        status = "ERROR"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{timestamp} - Website is {status}"
    
    print(log)

    with open("log.txt", "a") as file:
        file.write(log + "\n")

while True:
    check_website()
    time.sleep(10)