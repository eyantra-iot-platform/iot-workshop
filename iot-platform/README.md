## Learn to use e-Yantra IoT Platform

**e-Yantra IoT Platform** is a framework for building IoT applications faster. It takes care of common boilerplate like tasks 
so that you can concentrate on your business logic. 

It acts as a wrapper on top of AWS IoT and other AWS services. So you can connect your devices to IoT Platform the same way as 
you would connect them to AWS IoT. But don't worry if you have never used AWS IoT before, we still have you covered.

Here you will find code samples and resources to read from to use how to **connect your device to e-Yantra IoT Platform** (~AWS IoT). If your device or the platform isn't lsited
here you can check out [*aws-iot-device-sdk*](https://aws.amazon.com/iot/sdk/) for your platform. 

Along with that you also need to know how to actually **tell the platform about the things/devices** (micro-controllers or other connected devices) that you intend to use.
A notion of a thing will be sufficient if your application is small. But if you are building an application on a bigger scale to properly
manage your devices. For that we have organizational units provided in the platform namely, units, things, devices and device attributes. 
After you create a thing, you can download the information for the devices like certificates, thingID, etc. and connect them.

### As you can see, connecting devices actually is a two step process. For that reason we have grouped resources into two folders:
1. [**Using e-Yantra IoT Platform**](./using-iot-platform)
    
    Resources and necessary readings to create organizational units and provisioning things/devices that you wish to use.
   This part is essentially the same for any device you use be it Rpi, Arduino, ESP or your personal computer using whichever 
   language runtime (like Python, NodeJS, C).
   
2. [**Connecting devices to e-Yantra IoT Platform**](./iconnecting-devices-to-platform)

    Code samples and necessary readings to connect devices to IoT Platform using information obtained from previous steps.
    
In e-Yantra IoT workshops, we give kits to the participants over which they perform these hands-on exercises. In the end, they also a sample application. You can find them in the [**projects**](./projects) folder.
