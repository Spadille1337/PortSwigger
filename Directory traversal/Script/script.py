import sys
import requests
import time

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} domain")
    sys.exit(1)

URL = sys.argv[1]

f=open("dirlist.txt","r")

for l in f:
    payload = URL+l.strip()
    response=requests.get(payload)
    print(f"HTTP Status Code : {response.status_code} || Testing Path : {l}",end="")
    time.sleep(1)
