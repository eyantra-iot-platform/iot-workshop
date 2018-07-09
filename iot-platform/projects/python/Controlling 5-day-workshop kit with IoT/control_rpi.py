import threading
import time
import json
import ast
import RPi.GPIO as GPIO
import servo_control as ser
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


# Details about thing
THING_ID = "thing22"
CLIENT_ID = "MyRpi"
CERTIFICATE_PATH = "./certificates"
ENDPOINT = "akbmorjah98q5.iot.ap-southeast-1.amazonaws.com"


# LED PINs
LED_PIN_1 = 22
LED_PIN_2 = 17
LED_PIN_3 = 27

# Servo PINs
SERVO_PIN_1 = 23
SERVO_PIN_2 = 24

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(SERVO_PIN_1, GPIO.OUT)
GPIO.setup(SERVO_PIN_2, GPIO.OUT)

# Change to your topics here
UPDATE_TOPIC = "$aws/things/" + THING_ID + "/shadow/update"
DELTA_TOPIC = "$aws/things/" + THING_ID + "/shadow/update/delta"

ROOT_CA = CERTIFICATE_PATH + "/rootCA.pem"
PRIVATE_KEY = CERTIFICATE_PATH + "/private.key.pem"
CERTIFICATE_CRT = CERTIFICATE_PATH + "/certificate.crt.pem"

servo1 = ser.Servo(SERVO_PIN_1)
servo2 = ser.Servo(SERVO_PIN_2)



def get_init_mqtt_client(): 
	# Configuration for AWS IoT
	myMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
	myMQTTClient.configureEndpoint(ENDPOINT, 8883)
	myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE_CRT)


	# myMQTTClient.configureOfflinePublishQueueing(-1)  
	# Infinite offline Publish queueing
	# myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
	myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
	myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
	myMQTTClient.enableMetricsCollection()

	return myMQTTClient




def publish_sensor_data(interval, mqtt_client, servo1, servo2):	
	while True:
		# Dictionaries and messages for publishing
		publish_dict = {'state': {'reported': {'device24.65': get_sensor_values(), 
			'device24.66': servo1.get_value(),
			'device24.68': servo2.get_value()
		}}}
		publish_message = json.dumps(publish_dict)
		print "Message to publish:-", publish_message

		# Update device shadow
		published = mqtt_client.publish(UPDATE_TOPIC, publish_message, 0)
		print "Published:-", published

		# wait interval seconds before executing again
		time.sleep(interval)



def update_thing_state(client, userdata, message):
	print client, userdata, message
	message_dict = ast.literal_eval(message.payload)
	
	state = message_dict['state']
	if 'device24.65' in state:
		led = message_dict['state']['device24.65']
		if led == 0:
			GPIO.output(LED_PIN_1, True)
			GPIO.output(LED_PIN_2, False)
			GPIO.output(LED_PIN_3, False)
		elif led == 1:
			GPIO.output(LED_PIN_1, False)
			GPIO.output(LED_PIN_2, True)
			GPIO.output(LED_PIN_3, False)
		elif led == 2:
			GPIO.output(LED_PIN_1, False)
			GPIO.output(LED_PIN_2, False)
			GPIO.output(LED_PIN_3, True)
		elif led == 3:
			GPIO.output(LED_PIN_1, False)
			GPIO.output(LED_PIN_2, False)
			GPIO.output(LED_PIN_3, False)

	if 'device24.66' in state:
		print "Moving servo ..."
		angle = message_dict['state']['device24.66']
		servo1.set_value(angle)

	if 'device24.68' in state:
		print "Moving servo ...."
		angle2 = message_dict['state']['device24.68']
		servo2.set_value(angle2)
	
	# led = GPIO.input(LED_PIN_1)
	# publish_dict = {'state': {'reported': {'device24.65': led, 'device24.66': 12}}}
	# publish_message = json.dumps(publish_dict)
	# print "Message to publish:-", publish_message

	# # Update device shadow
	# published = mqtt_client.publish(UPDATE_TOPIC, publish_message, 0)


def get_sensor_values():
	return get_led_values()

def get_led_values():
	if GPIO.input(LED_PIN_1):
		led = 0
	elif GPIO.input(LED_PIN_2):
		led = 1
	elif GPIO.input(LED_PIN_3):
		led = 2
	else:
		led = 3
	return led 



if __name__ == "__main__":
	try:
		# Connect to MQTT broker
		mqtt_client = get_init_mqtt_client()
		print "Connected:-", mqtt_client.connect()
		
		# Start the thread
		t = threading.Thread(target=publish_sensor_data, args = (5, mqtt_client, 
			servo1, servo2))
		

		# Run the thread as a daemon which will die after parent dies 
		t.daemon = True
		t.start()
		
		mqtt_client.subscribe(DELTA_TOPIC, 0, update_thing_state)
		
		# To keep parent alive as long as ctrl + c
		while True:
			pass
	except KeyboardInterrupt:
		print "Cleaning up and exiting!"
		servo1.stop()
		servo2.stop()
		GPIO.cleanup()
