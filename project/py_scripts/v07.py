from lib.led_light import Led_Light
from lib.controller import TrafficLightSubsystem
from time import sleep

red = Led_Light(3, False, True)
amber = Led_Light(5, False, True)
green = Led_Light(6, False, True)

Light = TrafficLightSubsystem(red, amber, green, True)


def Traffic_Subsystem_Driver():
    print("Testing Traffic Light in 5 seconds")
    sleep(5)
    Light.show_red()
    print("Pass if: Red ON, Amber OFF & Green OFF")
    sleep(10)
    Light.show_amber()
    print("Pass if: Red OFF, Amber ON & Green OFF")
    sleep(10)
    Light.show_green()
    print("Pass if: Red OFF, Amber OFF & Green ON")
    sleep(10)


Traffic_Subsystem_Driver()
