
# Simulated MQTT consumer + API
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("MQTT recebido:", msg.payload)

client = mqtt.Client()
client.connect("mqtt",1883,60)
client.subscribe("sensores/#")
client.on_message = on_message
client.loop_start()
