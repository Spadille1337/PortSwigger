Firstly, Determine the number of columns that are being returned by the query and which columns contain text data same as we done in previous labs.

Now, use Payload:
```sql
' UNION SELECT NULL,username||'~'||password FROM users--
```

- Double pipe sequence (||) is string concatenation operator in Oracle. And tilde is used to separate the multiple values in one column.
