import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Thing information
THING_ID = "25"
CLIENT_ID = "myClientID" 
ENDPOINT = "akbmorjah98q5.iot.ap-southeast-1.amazonaws.com"
CERTIFICATE_PATH = "./certificates"

# Change to your topics here
UPDATE_TOPIC = "$aws/things/thing" + THING_ID + "/shadow/update"
DELTA_TOPIC = "$aws/things/thing" + THING_ID + "/shadow/update/delta"

ROOT_CA = CERTIFICATE_PATH + "/rootCA.pem"
PRIVATE_KEY = CERTIFICATE_PATH + "/private.key.pem"
CERTIFICATE_CRT = CERTIFICATE_PATH + "/certificate.crt.pem"


# Configuration for AWS IoT
myMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
myMQTTClient.configureEndpoint(ENDPOINT, 8883)
myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE_CRT)
# myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
# myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myMQTTClient.enableMetricsCollection()


# Connect to MQTT broker
connected = myMQTTClient.connect()
print("Connected: ", connected)


# Dictionaries and messages for publishing
publish_dict = {'state': {'reported': {'device26.69': 29, 'device26.70': 12.0, 'device27.71': 'Hello World!'}}}
publish_message = json.dumps(publish_dict)
print("Message to publish: ", publish_message)

def print_message(client, usrData, msg):
    print(msg.payload)

# Listen for state change
myMQTTClient.subscribe(DELTA_TOPIC, 1, print_message)

# Update device shadow
published = myMQTTClient.publish(UPDATE_TOPIC, publish_message, 0)
print("Published: ", published)
