import paho.mqtt.client as mqtt
import json
import boto3

MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/BedRoom/#"
#kinesis = boto3.client('kinesis')

def on_connect(mosq,obj,flags,rc):
    mqttc.subscribe(MQTT_Topic,0)

def on_message(mosq,obj,msg):
    print("MQTT Data Received: ")
    print("MQTT Topic: " + msg.topic)
    print(msg.payload)
    if msg.topic == "Home/BedRoom/DHT22_Temperature":
        jsonData = msg.payload
        json_Dict = json.loads(jsonData)
        #SensorID - json_Dict['Sensor_ID']
        json_Dict = json.dumps(json_Dict)
        print(jsonDict)
        #kinesis.put_record(
        #    StreamName = "TemperatureStream"
        #    Data = json_Dict
        #    PartirionKey = "partitionkey"
        #)
def on_subscribe(mosq,obj,mid,granted_qos):
    pass
mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

mqttc.loop_forever()
