# Script MUST be run with python 2.7 and opencv 2.4
# Script is run on a desktop pc, x,y values are sent to raspberry pi for servo control.

import time
import cv2
import paho.mqtt.client as mqtt

# Define MQTT Variables
MQTT_HOST = "10.0.0.39" # My Raspberry Pi wLan address
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "face_tracking"

# Define on_publish event function
def on_publish(client, userdata, mid):
 print "MQTT: "

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

# Initialize OpenCV
FCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

while True:
	ret, frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	Fsearch = FCascade.detectMultiScale(
		gray,
		scaleFactor=1.3,
		minSize=(40,40),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	for(x,y,w,h) in Fsearch:
		rect = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0),2)
		x1 = (int(x)*.3) #collect x values 
		y1 = (int(y)*.3) #collect y values
		MQTT_MSG = 'x'+str(x1)+'y'+str(y1) #Send values to be parsed on RPi
		print'x:', x1
		print'y:', y1
		
		# Publish message to MQTT Broker 
		mqttc.publish(MQTT_TOPIC,MQTT_MSG)
		
	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
video_capture.release()
mqttc.disconnect() # Disconnect from MQTT_Broker
cv2.destroyAllWindows()

