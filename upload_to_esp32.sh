set -e
echo 'Trying to guess where the ESP32 is connected...'

esp32_ttyUSB="$(dmesg | grep ttyUSB | grep cp210x | grep attached | awk 'NF>1{print $NF}' | tail -n 1)"

if [ -n "${esp32_ttyUSB}" ]; then
    echo "Assuming your ESP32 is connected to ${esp32_ttyUSB}."
    echo "Copying data over..."
    rshell --buffer-size 30 --port /dev/${esp32_ttyUSB} cp -r ./src/* /pyboard/
    echo "Done!"
else
    echo "Couldn't find a connected ESP32."
    echo "Try running 'dmesg | grep ttyUSB' and see if you find it."
fi