# A NodeJS app on Raspberry Pi that sends and receives arbitrary data to AWS IoT

## Overview
This is a project to send arbitrary data to AWS IoT. It publishes data to thing shadow service in AWS IoT.

## Steps:
 1. Login to IoT dashboard available in following [link](http://iot.e-yantra.com) with the provided user id and password
 2. Create a thing in the dashboard 
 3. Create devices under thing as:
     * Temperature, double
     * Humidity, double
[[./assets/adding_device.png|adding devices]]
 4. Download certificates and keep them in a separate folder
 5. View the thing properties by clicking GENERATE CLIENT button in dashboard. 
[[./assets/Thing_properties.png]]
Note the clientID and deviceXX.XX in the pop-up. In later instruction these will be needed in the code.
 6. In explorer, go to *interfacing-AWS-IoT/RPi/test-js/* folder. See [this](https://github.com/sanamshakya/interfacing-AWS-IoT/blob/master/RPi/test-js/)
 7. Run command "npm init" and fill the fields you require (optionally, you can also skip through all of them).
 8. Run command "npm install aws-iot-device-sdk --save".
 7. Copy downloaded files: certificate.crt.pem, private.key.pem, public.key.pem and rootCA.pem in test-js folder
 8. Edit test.js file present in test-js folder by replacing " " with the required values according to thing settings found in step 5.
 9. For now we will supply arbitrary values to iot platform. For it, we will replace fields enclosed in "< >" by integers or doubles ( e.g. <device-attribute> becomes 19 and so on).
 10. In terminal go to test-js folder and run command "node test.js" to start the app.
 11. Go to dashboard, check if values are updated. 
