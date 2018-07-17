## Writing notification rules

Notification rules allow devices to send a notification on a certain trigger condition. You have the option to specify any trigger condition that you may like. 

For example, you might want to be notified if temperature on your sensor goes above some X degrees. You can create an SNS rule with the condition for temperature greater than X and message you want to send. You can also add subscribers by email, sms*, etc. to receive this notification. 

Prerequisites
-----
1. Creating [organizational units](./1-creating-organizational-units.md) with actuators in IoT Platform.
2. [Connecting a thing](../connecting-devices-to-platform/python/1-connecting-devices-to-platform-python.md) (micro-controllers, connected devices) to IoT Platform and make it trigger actions (like LED on/off, etc).

Steps
-----
1. Login to *e-Yantra IoT Platform*.
2. Select the *thing* you wish to create a notification rule on.
3. Find the *Rules section* and click on *Create rule* button.
![Rules section](./assets/rules-section.png)
4. You will see a modal like below. Following are the fields:
    1. **Name** is the name of your rule. It CANNOT BE SPACE SEPERATED. You should use hypens or underscores if you inted to create multi-word string.
    2. **Description** is the description of what your rule does.
    3. **Data** is how much of your data from the device should be used for making decisions and sending. If you want to select all the data, you can use "*" for ALL.
    4. **Condition** is trigger condition on which the rule executes the action (in our case sends an email/sms). You can only put condition on any of the fields filtered due by data parameter.
5. We will create a rule named Temperature rule. Fill the values like shown below.
    **Note:** We have to use *get* method to fetch value from device shadow of the temperature field.
![Create SNS 1](./assets/create-sns.png)
6. Select *SNS* in Type and fill the details like below. Following are what the fields mean:
    1. **SNS Topic** on which you want to publish this message. It CANNOT BE SPACE SEPERATED. You should use hypens or underscores if you inted to create multi-word string.
    2. **Subject** for notifications that *support subject field* like emails.
    3. **Message** to send as a payload in emails/sms.
    4. **Interval** is minimum time before another notification is sent.
![Create SNS 2](./assets/create-sns-2.png)
7. Save your rule and that's it. The rule has been created but there are no subscirbers for your rule.
8. Click on the details button and you would see this window. 