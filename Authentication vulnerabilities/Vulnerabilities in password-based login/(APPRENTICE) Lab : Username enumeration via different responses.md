Step 1 : Navigate to login page of the given lab.

Step 2 : Enter any random `username` and `password` and send and in parallel intercept this request using BurpSuite.

Step 3 : Send this intercepted request to `Intruder` tab.

Step 4 : Choose Attack type `Sniper` and click on `Clear §`. Then choose the value of parameter `username` and click on `Add §`. Next, Go to `Payloads` sub-tab, choose Payload type as `Simple List` and next paste the given usernames list in the `Payload Options` box. Now go back to `Positions` tab and click on `Start Attack`. The attack will start in a new window. Now, you can observe the difference between correct username ot incorrect username either on the basis of status code, length, error or timeout. In this given lab, if we cling on length heading then we will get the output in some arrange manner.

Step 5 : We observe that the payload `akamai`(in this cas only) has different length than other payloads. So, we can check it by entering `affiliate` as username and something random as password. So, it will show that `Incorrect Password` instead of `Incorrect Username`. So, this confirms that, we are on right path.

Step 6 : Repeat Step 4 in terms of Password but enter the username that you find from the above steps.

Step 7 : Observe the status code. The one with different status code is the correct password. Login to the given page to complete the lab.
