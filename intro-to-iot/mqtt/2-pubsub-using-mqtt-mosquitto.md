## Install Mosquitto MQTT Broker (on Linux Machine - tested for (Ubuntu 16.04 LTS (Xenial  Xerus ))

1. Add the Mosquitto-dev PPA to repositories list

    `sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa`

2. Update Package Repository

    `sudo apt-get update`

3. Install Mosquitto MQTT Broker

    `sudo apt-get install mosquitto`

    `sudo apt-get install mosquitto-clients`

4. Starting the Mosquitto broker

    `sudo /etc/init.d/mosquitto start`

5. Stopping the broker

    `sudo /etc/init.d/mosquitto stop`

6. Checking status of the broker

    `sudo /etc/init.d/mosquitto status`

7. Configuration (Leave it default if you are new to MQTT)

        a. Configuration file of the Mosquitto broker is located at :/etc/mosquitto/mosquitto.conf

        b. The default TCP port of the broker is 1883 which is used for the ‘mqtt’ scheme. The default TCP port of the broker is 8883 which is used for the ‘mqtts’ scheme. Make sure those ports are not blocked by your firewall.

8. Testing the Mosquitto MQTT Broker

                1. Subscribe on the topic: "XYZ". Open a new terminal window and type following command

                   mosquitto_sub -h localhost -t "XYZ" 

                2. Publish on the topic: "XYZ". Open a new terminal window and type following command

                   mosquitto_pub -t XYZ -m "ERTS LAB"

## Some more examples

* Subscribe on the topic: sensor/dht11/temperature

    `mosquitto_sub -h localhost -t  sensor/dht11/temperature`

* Subscribe on the topic: sensor/dht11/humidity

    `mosquitto_sub -h localhost -t  sensor/dht11/humidity`

* Publish on the topic: sensor/dht11/temperature and sensor/dht11/humidity separately

    `mosquitto_pub -t sensor/dht11/temperature -m 25`
    
    `mosquitto_pub -t sensor/dht11/humidity -m 94`

## Example of wildcard subscription

* Subscribe on the topic: sensor/+/temperature

    `mosquitto_sub -h localhost -t  sensor/+/temperature`

* Subscribe on the topic: sensor/#

    `mosquitto_sub -h localhost -t  sensor/#`

* Publish on the topic: sensor/dht11/temperature and sensor/dht22/temperature

    `mosquitto_pub -t sensor/dht11/temperature -m 25`

    `mosquitto_pub -t sensor/dht22/temperature -m 20`


### LWT example
* Subscribe on the topic: report/connection_lost

    `mosquitto_sub -h localhost -t  report/connection_lost`

* Open terminal and type following

   `mosquitto_sub -d -h localhost -t sensor/dht11/temperature --will-topic report/connection_lost --will-payload "Problem reported"`

Close this terminal (or press ctrl c) and check output in terminal which is subscribed to topic report/connection_lost