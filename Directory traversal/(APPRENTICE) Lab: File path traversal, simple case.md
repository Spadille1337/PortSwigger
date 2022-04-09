Use the following payload:
```
https://acd21f2c1ec584c7c0a59582003100c1.web-security-academy.net/image?filename=../../../etc/passwd
```
Note : The image files themselves are stored on disk in the location `/var/www/images/`. The application implements no defenses against directory traversal attacks, so an attacker can request the following URL to retrieve an arbitrary file from the server's filesystem. The sequence `../` is valid within a file path, and means to step up one level in the directory structure. The three consecutive `../` sequences step up from `/var/www/images/` to the filesystem root, and so the file that is actually read is: `/etc/passwd`
