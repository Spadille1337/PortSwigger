Step 1 : Navigate to login page of the given lab.

Step 2 : Enter any random `username` and `password` and send and in parallel intercept this request using BurpSuite.

Step 3 : Send this intercepted request to `Intruder` tab.

Step 4 : Choose Attack type `Sniper` and click on `Clear §`. Then choose the value of parameter `username` and click on `Add §`. Next, Go to `Payloads` sub-tab, choose Payload type as `Simple List` and next paste the given usernames list in the `Payload Options` box. Next, go to `Options` tab under `Grep - Extract`, click `Add`. In this dialog box appears, scroll down and highlight the text `Invalid username or password.` ans click `OK`. Now go back to `Positions` tab and click on `Start Attack`. The attack will start in a new window. Now, you can observe the difference between correct username ot incorrect username either on the basis of status code, length, error or timeout. In this given lab, if we lab, we will check for error message. In these error messages, we will notice : `You have made too many incorrect login attempts. Please try again in 30 minute(s)` as response so it may be possible that our IP address is being blocked because of many requests at a time.

Step 5 : Identify that the `X-Forwarded-For` header is supported, which allows you to spoof your IP address and bypass the IP-based brute-force protection.

Step 6 : Send the request to Burp Intruder and select the attack type to `Pitchfork`. Clear the default payload positions and add the X-Forwarded-For header. Add payload positions for the X-Forwarded-For header and the username

Step 7 : On the Payloads tab, select payload set 1. Select the Numbers payload type. Enter the range 1 - 100 and set the step to 1. Set the max fraction digits to 0. This will be used to spoof your IP. Select payload set 2 and add the list of usernames. Start the attack.

Step 8 : Notice that one of the response times was significantly longer than the others. Repeat this request a few times to make sure it consistently takes longer, then make a note of this username.

Step 9 : Repeat Step 5,6,7 in terms of Password but enter the username and that you find from the above steps.

Step 10 : Observe the status code. Login to the given page to complete the lab.
