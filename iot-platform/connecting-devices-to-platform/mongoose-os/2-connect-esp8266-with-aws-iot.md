# A Mongoose OS app that sends DHT sensor data to AWS-IOT

## Overview
This is a project to send DHT data to AWS-IOT. It publishes data to a thing shadow in AWS-IOT. It also has a handler to turn on or off the on-board ESP8266 LED.

## Steps:
 1. Login to IoT dashboard available in following [link](http://iot.e-yantra.com/login) with the provided user id and password
 2. Create a thing in the dashboard 
 3. Create devices under thing as:
     * Temperature, double
     * Humidity, double
     * LED, boolean, actuator
[[/assets/adding_device.png|adding devices]]
 4. Download certificates and keep them in a separate folder
 5. View the thing properties by clicking GENERATE CLIENT button in dashboard. 
[[/assets/Thing_properties.png]]
Note the clientID and deviceXX.XX in the pop-up. In later instruction these will be needed in the code.
 6. In expolorer, go to *interfacing-AWS-IoT/esp/mongoose/aws-dht-js* folder
 7. Copy downloaded files: certificate.crt.pem, private.key.pem, public.key.pem in aws-dht-js/fs folder
 8. Edit conf1.json file present in aws-dht-js/fs by replacing "???" with the required values according to thing settings found in step 5.
 9. Now edit the init.js file by replacing "??.??" with the required values as found in step 5.
 10. Connect the DHT sensor by connecting:

 | DHT pins | ESP8266 Dev Kit pins |
 |--------- | ---------------------- |     
 |      + | 3.3V |
 |      out | GPIO5 |
 |       - | GND |

Refer diagram below for pinout of ESP8266 NodeMCU DevKit

[[assets/nodemcu_pins.png]]
 
 11. In terminal go to aws-dht-js folder to build and flash the app
 12. Go to dashboard, check if values are updated and control the led 




