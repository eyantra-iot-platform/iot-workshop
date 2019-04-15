This wiki contains the instruction and links for using Mongoose OS with ESP8266. You will setup a build environment and run a demo-js app. 

First of all Clone or download the github [repo](https://github.com/sanamshakya/interfacing-AWS-IoT) before going through further instructions. All the required codes for workshop are available in the above repo.

# Mongoose OS
An open source operating system for hardware that support javascript. It follows event-driven architecture with a non-blocking I/O model.

## Features
* Supported microcontrollers: ESP32, ESP8266, CC3220, CC3200
* based on Mongoose library for networking
* APIs for GPIO, PWM and other peripherals 
* Built in support for IoT cloud integration
* Manage devices using Remote Procedure Call(RPC)
* Write firmware in Javascript or in C
* Supports Over the Air(OTA) firmware update

For further information on Mongoose OS is available on the following [link](https://mongoose-os.com/)

# Mongoose OS components
* **mos tool** - device management and firmware building
* **build toolchain (only for building firmware offline)** - Docker image for building a mongoose OS app (normally happens in cloud unless specified otherwise)
* **ready-to-use apps and libraries**

# Hardware and Softwares
* Hardware required: ESP8266 or ESP32
* Software required: mos tool

# Installing mos tool
Follow instruction in given link to install mos tool
https://mongoose-os.com/docs/mongoose-os/quickstart/setup.md#1-download-and-install-mos-tool

# Running the demo-js app

## Getting the demo-js app
In terminal goto *interfacing-AWS-IoT/esp/mongoose/demo-js* directory which contains code and configuration file for app

## Mongoose OS app structure
* mos.yml
* fs/init.js *//if app is developed using JavaScript*
* src/main.c *//if app is developed using C*

## Using mos tool
* Command for building app

In terminal, in *demo-js* app directory, run following command to build the app

`mos build --arch=esp8266` 

This will trigger a remote build process and create a new *build* folder with the fs(filesystem) and fw(firmware) folders required for the app.

* Flashing the firmware and filesystem
Connect ESP/NodeMCU to USB port with the provided cable. New serial device will be detected in host system, generally as */dev/ttyUSB0*. To flash the code type following command in the terminal.

`sudo mos flash` 

In Linux, for flashing the firmware mos tool uses *ttyUSB0* serial port of the system. 
To see the available serial ports in host system, you can use `ls /dev/ttyUSB*` command.
If device is detected other than ttyUSB0, change the default serial port by specifying the value manually with *--port* flag. 

`sudo mos flash --port /dev/ttyUSB1`

## More mos commands 
* mos --help *//for help on use of various mos commands*
* mos wifi \<Wifi SSID\> \<Wifi Password\> *//for setting the wifi connection with access point*
* mos console *//for viewing the console log of running app for debugging*
* mos ls *//list the filesystem in the device*
* mos config-get *//list the configuration setting for all peripherals and app*
* mos config-set \<config tag = value\> *//for changing the value in the configuration file*
e.g. for enabling mqtt - `mos config-set mqtt.enable=true`







