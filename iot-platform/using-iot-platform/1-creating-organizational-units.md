## Using IoT Platform

In this tutorial you will learn to create organizational units in e-Yantra IoT Platform.

When you are creating IoT projects you might want to divide the things into groups so that you can manage them better. IoT platform realizes this use case and provides various organisational units for you to use.

There are 4 main organizational units as such as:
1. Units

Units can contain other units and things.

2. Things

Things repersent your micro-controllers which will be connected to internet and send/recv data. A thing can have one or more devices.

3. Devices

Devices are sensors that you connect to a thing example a DHT sensor to measure temperature or humidity.
A device can have one or more device attributes.

4. Device Attributes

Device attributes are the quantities a sensor measures. It can be more than one like in DHT, it is temperature as well as humidity. It has a type which is one of Boolean, Integer, String, Double. You can choose to make it either actuator or sensor.

You can create, read, update or delete each of these. We will be seeing how to do that with an example.

Goal:
To create a unit "IoT Lab" with a single thing "Rpi" with two devices "LED" and "DHT". 
"LED" will have a single device attribute of type boolean. "DHT" will have two attributes, temperature and humidity one integer and another double.

Solution:

