## Controlling servos and LEDs on 5-day-workshop kit with IoT

We will be interfacing the 5-day-workshop kit with IoT Platform. With this we will be able to control the hardware mounted on the kit, like servos, LEDs and also read sensor data, from IoT Platform or even mobile devices using IoT Platform REST Api.

You have already learned controlling connected hardware on the previous days. So we will mostly be concentrating on the IoT part.

The Kit
-----
![5-day-workshop kit](./assets/workshop-kit.jpeg)

Lets get started
-----
1. Download or clone this repo and change directory to the projects folder.
(You can either do it on your Rpi directly or you can move the project files after modifying them on your computer).
2. Next go ahead and create a thing for this Rpi in IoT Platform. You have to create 3 devices:
- ServoH: Should have one integer device attribute which needs to be an actuator.
- ServoV: Should have one integer device attribute which needs to be an actuator.
- LED: Should have one integer device attribute which needs to be an actuator too.

Check this to know more about how you can do it.

3. Once that is done and your thing is created, you should download certificates for it and put them in certificates folder under projects.
4. Next open control_rpi.py file using a text editor and change below settings to what you can find on "generate client" tab.
5. Also change the dictionary with values in device-shadow JSON shown yet again in the "generate client" tab.
6. Run the python program. If it gives you no error your client is set.
7. Go to IoT Platform, select the thing you created and click on dashboard button.
8. You should see controls for the hardware on Rpi.
9. Change values on the controls to see the servos and LEDs actuating.

If you got it to work, then congrats. Raise your ✋ and pat your back.

