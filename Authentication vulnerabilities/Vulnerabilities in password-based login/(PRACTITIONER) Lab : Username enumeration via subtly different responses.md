Step 1 : Navigate to login page of the given lab.

Step 2 : Enter any random `username` and `password` and send and in parallel intercept this request using BurpSuite.

Step 3 : Send this intercepted request to `Intruder` tab.

Step 4 : Choose Attack type `Sniper` and click on `Clear §`. Then choose the value of parameter `username` and click on `Add §`. Next, Go to `Payloads` sub-tab, choose Payload type as `Simple List` and next paste the given usernames list in the `Payload Options` box. Next, go to `Options` tab under `Grep - Extract`, click `Add`. In this dialog box appears, scroll down and highlight the text `Invalid username or password.` ans click `OK`. Now go back to `Positions` tab and click on `Start Attack`. The attack will start in a new window. Now, you can observe the difference between correct username ot incorrect username either on the basis of status code, length, error or timeout. In this given lab, if we lab, we will check for error message.

Step 5 : When the attack is finished, there is an additional column containing the `error message` you extracted. Sort the results using this column to notice that one of them is subtly different. We observe that the payload `ads`(in this case only) has different error message (basically a typoerror) than other payloads. 

Step 6 : Repeat Step 4 in terms of Password but enter the username and that you find from the above steps.

Step 7 : Observe the error message. The one with different no error message is the correct password. Login to the given page to complete the lab.
