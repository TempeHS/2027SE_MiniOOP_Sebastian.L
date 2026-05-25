from lib.led_light import led_light
from time import sleep

red_light = led_light(3, True, True)
while True:
    red_light.flash()
    print(1)
    sleep(0.1)
