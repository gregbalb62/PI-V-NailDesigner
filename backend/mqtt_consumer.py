
import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print("Salvar no banco:", data)

client = mqtt.Client()
client.connect("mqtt",1883,60)
client.subscribe("sensores/#")
client.on_message = on_message
client.loop_forever()
