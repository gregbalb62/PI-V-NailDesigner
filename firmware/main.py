
from umqtt.simple import MQTTClient
import time

client = MQTTClient("esp32","BROKER_IP")

while True:
    payload = '{"pressao":12,"nivel":30,"vazao":7}'
    client.connect()
    client.publish("sensores/data", payload)
    client.disconnect()
    time.sleep(5)
