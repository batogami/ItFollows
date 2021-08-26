import RPi.GPIO as GPIO
import time

class Ultra_Sonic_Sensor():

    def __init__(self, trigger_pin, echo_pin):
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin

        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.output(self.trigger_pin, False)

    def distance(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)
        start = time.time()
        stop = time.time()
        while GPIO.input(self.echo_pin) == 0:
            start = time.time()
        while GPIO.input(self.echo_pin) == 1:
            stop = time.time()
        # GPIO.wait_for_edge(self.echoPin, GPIO.FALLING, timeout=100)
        stop = time.time()
        return ((stop - start) * 34300.0) / 2.0

