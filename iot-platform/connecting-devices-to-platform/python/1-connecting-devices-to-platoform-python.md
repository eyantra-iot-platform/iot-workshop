## Connecting devices to IoT platform with python

You will learn to connect your device, that supports python, to IoT Platform(~AWS IoT). 

We will be using one of the popular devices out there which is Raspberry Pi. But please note that the procedure is 

going to remain the same as long as you are using Python.

**NOTE:** We will need some files and information before hand like certificate pairs, thingID, etc. This becomes available only after you create a thing in IoT Platform.

For instructions on how to do it please see [*Using IoT Platform*](../../using-iot-platform).

Lets get started:
-----
1. Create a folder that will hold all your project files. We will name it `iot-app`
2. `cd iot-app` and paste all **4 certificate related files inside** it in **a folder named "certificates"** namely, *private.key.pem, public.key.pem, certificate.crt.pem and rootCA.pem*.
3. Next you have to download the file [*simple-pubsub.py*](./simple-pubsub.py). You can either copy paste the contents of this file or clone the full repository and extract it.
4. Copy this file into `iot-app` folder.
5. Open the file and change these contents.
