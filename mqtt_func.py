import paho.mqtt.client as mqtt
broker_address = "broker.mqtt.cool"
port = 1883
subscribe_topic = "dht11"
rec_msg = None


def publish_data(publish_topic, payload):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"Publisher")
    client.connect(broker_address, port)
    client.publish(publish_topic, payload)
    # print("Published data:", payload,"on : ",publish_topic)



# # Callback function when message is received
# def on_message(client, userdata, message):
#     payload = message.payload.decode()
#     global rec_msg 
#     rec_msg = payload
#     # print("Received:", payload)
#     client.disconnect()

# def temprature_data():
#     return rec_msg

# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"Subscriber")# Create MQTT Client
# client.on_message = on_message  # Assign on_message callback
# client.connect(broker_address, port) # Connect to Broker
# client.subscribe(subscribe_topic)# Subscribe to topic
# client.loop_forever()# Loop to keep the client running until a message is received

if __name__ == "__main__":
    publish_data("eyantra",'1') 
    print(rec_msg[16:22])
    
        
