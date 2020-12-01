""" #import paho.mqtt.client as mqtt
#import json
#import boto3

#MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/BedRoom/#"
kinesis = boto3.client('kinesis','us-east-1')

def on_connect(mosq,obj,flags,rc):
    mqttc.subscribe(MQTT_Topic,0)

def on_message(mosq,obj,msg):
    print("MQTT Data Received: ")
<<<<<<< HEAD
 #   print("MQTT Topic: " + msg.topic)
 #   print(msg.payload)
 #   if msg.topic == "Home/BedRoom/DHT22_Temperature":
 #       jsonData = msg.payload
 #       json_Dict = json.loads(jsonData)
        #SensorID - json_Dict['Sensor_ID']
 #       json_Dict = json.dumps(json_Dict)
 #       print(jsonDict)
        #kinesis.put_record(
        #    StreamName = "TemperatureStream"
        #    Data = json_Dict
        #    PartirionKey = "partitionkey"
        #)
#def on_subscribe(mosq,obj,mid,granted_qos):
#    pass
#mqttc = mqtt.Client()
=======
    print("MQTT Topic: " + msg.topic)
    print(msg.payload)
   # if msg.topic == "Home/BedRoom/DHT22_Temperature":
    jsonData = msg.payload
    json_Dict = json.loads(jsonData)
        #SensorID - json_Dict['Sensor_ID']
    data = json.dumps(json_Dict)
    print(data)
    kinesis.put_record(
        StreamName = "kinesis-analytics-demo-stream",
        Data = data,
        PartitionKey = "partitionkey"
        )
def on_subscribe(mosq,obj,mid,granted_qos):
    pass
mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
>>>>>>> 1745018f0962ffe098bd2d55841a7538c4988e31

#mqttc.on_message = on_message
#mqttc.on_connect = on_connect
#mqttc.on_subscribe = on_subscribe

#mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

#mqttc.loop_forever()
*/
"""
import json
import boto3
import random
import datetime
kinesis = boto3.client('kinesis', 'us_east_1')
def getReferrer():
    data = {}
    now = datetime.datetime.now()
    str_now = now.isoformat()
    data['EVENT_TIME'] = str_now
    data['TICKER'] = random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV'])
    price = random.random() * 100
    data['PRICE'] = round(price, 2)
    return data
while True:
    data = json.dumps(getReferrer())
    print(data)
    kinesis.put_record(
        StreamName="kinesis-analytics-demo-stream",
        Data=data,
        PartitionKey="partitionkey"
        )