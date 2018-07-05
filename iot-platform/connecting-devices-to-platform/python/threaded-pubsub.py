import threading
import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Details about thing
THING_ID = "thing22"
CLIENT_ID = "MyRpi"
CERTIFICATE_PATH = "./certificates"
ENDPOINT = "akbmorjah98q5.iot.ap-southeast-1.amazonaws.com"


# Change to your topics here
UPDATE_TOPIC = "$aws/things/" + THING_ID + "/shadow/update"
DELTA_TOPIC = "$aws/things/" + THING_ID + "/shadow/update/delta"

ROOT_CA = CERTIFICATE_PATH + "/rootCA.pem"
PRIVATE_KEY = CERTIFICATE_PATH + "/private.key.pem"
CERTIFICATE_CRT = CERTIFICATE_PATH + "/certificate.crt.pem"


# Configuration for AWS IoT
myMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
myMQTTClient.configureEndpoint(ENDPOINT, 8883)
myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE_CRT)


myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myMQTTClient.enableMetricsCollection()


# Connect to MQTT broker
connected = myMQTTClient.connect()
print("Connected:-", connected)


def publish_sensor_data(interval):	
	try:
		while True:
			# Dictionaries and messages for publishing
			publish_dict = {'state': {'reported': {'device24.65': 29, 'device24.66': 12}}}
			publish_message = json.dumps(publish_dict)
			print("Message to publish:-", publish_message)

			# Update device shadow
			published = myMQTTClient.publish(UPDATE_TOPIC, publish_message, 0)
			print("Published:-", published)

			# wait interval seconds before executing again
			time.sleep(interval)
	except:
		print("Force closing ....")
		threading.current_thread().interrupt()


def update_thing_state(client, userdata, message):
	print(client, userdata, message)

	# Message payload is of type bytes
	print("Message payload:", dict(message.payload))
	print("Message topic:", message.topic)


if __name__ == "__main__":
	t = threading.Thread(target=publish_sensor_data, args = (5,))
	t.start()

	myMQTTClient.subscribe(DELTA_TOPIC, 0, update_thing_state)