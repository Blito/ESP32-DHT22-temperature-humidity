from time import sleep
from umqtt.mqtt_client import MQTTClient
from machine import Pin
from dht import DHT22

CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'sensors/temp_humidity'

def run(server_ip, publish_every_seconds = 60):
    client = MQTTClient(CLIENT_ID, server_ip)
    client.connect()

    sensor = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))

    while True:
        try:
            sensor.measure()
            t = sensor.temperature()
            h = sensor.humidity()

            if isinstance(t, float) and isinstance(h, float):
                msg = (b'{0:3.1f},{1:3.1f}'.format(t,h))
                client.publish(TOPIC, msg)
            else:
                print('Invalid sensor readings.')
        except OSError as e:
            print('Failed to read sensor.' + str(e))
        sleep(publish_every_seconds)