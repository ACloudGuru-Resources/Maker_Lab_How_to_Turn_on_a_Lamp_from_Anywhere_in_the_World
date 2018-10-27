import greengrasssdk
import RPi.GPIO as GPIO

# Greengrass client setup
client = greengrasssdk.client('iot-data')

# Relay pin on RPi
relayTriggerPin = 17

def function_handler(event, context):
    # Setup RPi GPIO 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relayTriggerPin, GPIO.OUT)

    # Detect the current pin state (On/Off)
    state = GPIO.input(relayTriggerPin)
    
    # Turn Lamp on
    if (state == 1):
        GPIO.output(relayTriggerPin, GPIO.LOW)
    # Turn Lamp off 
    else:
        GPIO.output(relayTriggerPin, GPIO.HIGH)
    
    return
