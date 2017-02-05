# Import package
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

#Servo Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
sx = GPIO.PWM(12, 50)
sx.start(7)


# Define MQTT Variables
MQTT_HOST = "10.0.0.39"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "face_tracking"
MQTT_MSG = "hello MQTT"

# Define on connect event function
# We shall subscribe to our Topic in this function
def on_connect(mosq, obj, rc):
 mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_message event function. 
# This function will be invoked every time,
# a new message arrives for the subscribed topic 

def on_message(mosq, obj, msg):
#Our actions need to take place within the message loop
 print "Topic: " + str(msg.topic)
 print "QoS: " + str(msg.qos)
 print "Payload: " + str(msg.payload)
 
 values = str(msg.payload)
 
 for i in values:
	 if i == 'x':
		servoX = values.rsplit('y',1)[0] 
		servoY = values.split("y",1)[1]
		
		for i in servoX:
			if i == 'x':
				servoX1 = servoX[1:]
	
		print servoX1
		print servoY
	
		x_value = servoX1
		y_value = servoY
		
		degree_X = 7
		degree_Y = 7
		
	 if servoX1 > '50.0':
		degree_X -= .02
		sx.ChangeDutyCycle(degree_X)
		time.sleep(.02)
		#print 'over 50'
		
	 elif servoX1 < '50.0':
		degree_X += .02
		if degree_X == 1:
			degree_X += 1
		sx.ChangeDutyCycle(degree_X)
		time.sleep(.02)
		#print 'under 50'
		

def on_subscribe(mosq, obj, mid, granted_qos):
 print("Subscribed to Topic: " + 
 MQTT_MSG + " with QoS: " + str(granted_qos))

# Initiate MQTT Client
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)



# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()




#Parse MQTT payload

for i in values:
	 if i == 'x':
		servoX = values.rsplit('y',1)[0] 
		servoY = values.split("y",1)[1]
		
		for i in servoX:
			if i == 'x':
				servoX1 = servoX[1:]
	
		print servoX1
		print servoY
	
		x_value = servoX1
		y_value = servoY
		
		degree_X = 7
		degree_Y = 7
		
	 if servoX1 > '50.0':
		degree_X += 0.009
		sx.ChangeDutyCycle(degree_X)
		time.sleep(.02)
		print 'over 50'
		
	 elif servoX1 < '50.0':
		degree_X -= 0.009
		sx.ChangeDutyCycle(degree_X)
		time.sleep(.02)
		print 'under 50'
		
		
		


	
	


