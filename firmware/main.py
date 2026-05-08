
import time
from umqtt.simple import MQTTClient

client = MQTTClient("esp32","BROKER_IP")

while True:
    data = '{"pressao":10,"nivel":20,"vazao":5}'
    client.connect()
    client.publish("sensores/data", data)
    client.disconnect()
    time.sleep(5)
