Firstly, Determine the number of columns that are being returned by the query and which columns contain text data same as we done in previous labs.

To verify the query is returning two columns, and both of which contain text:
`' UNION SELECT 'a','a' FROM DUAL--`

_DUAL is a table automatically created by Oracle Database along with the data dictionary. DUAL is in the schema of the user SYS but is accessible by the name DUAL to all users._

Now, use Payload:
```sql
' UNION SELECT BANNER, NULL FROM v$version--
```
_The version information is stored in a table called v$version._
