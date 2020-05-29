# main.py runs automatically in the ESP32 after boot.py finishes.

import dht_publish
import wifi
from config.network import SERVER, SSID, PASSWORD
from config.dht22 import PUBLISH_PERIOD

wifi.connect(SSID, PASSWORD)

dht_publish.run(SERVER, PUBLISH_PERIOD) 
