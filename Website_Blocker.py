import time
from datetime import datetime as dt 
hosts_location=r"C:\Windows\System32\drivers\etc"
hosts_temp="hosts"
blocked_websites=['www.facebook.com','facebook.com']
redirect="127.0.0.1"

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working Hours....")
        with open("hosts","r+") as file:
            content=file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+"\t"+website+"\n")
    else:
        print("Fun Time...")
        with open("hosts","r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)

