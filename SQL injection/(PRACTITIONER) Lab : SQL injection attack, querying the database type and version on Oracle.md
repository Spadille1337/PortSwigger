Firstly, Determine the number of columns `'UNION SELECT NULL,NULL FROM dual--+` that are being returned by the query and which columns contain text data `'UNION SELECT 'a','a' FROM dual--+` same as we done in previous labs.

To verify the query is returning two columns, and both of which contain text:
`' UNION SELECT 'a','a' FROM DUAL--`

**Note** : _On Oracle databases, every SELECT statement must specify a table to select FROM. If your UNION SELECT attack does not query from a table, you will still need to include the FROM keyword followed by a valid table name.
There is a built-in table on Oracle called dual which you can use for this purpose. For example: UNION SELECT 'abc' FROM dual. 
DUAL is a table automatically created by Oracle Database along with the data dictionary. DUAL is in the schema of the user SYS but is accessible by the name DUAL to all users._

Now, use Payload:
```sql
' UNION SELECT BANNER, NULL FROM v$version--
```
_The version information is stored in a table called v$version._
