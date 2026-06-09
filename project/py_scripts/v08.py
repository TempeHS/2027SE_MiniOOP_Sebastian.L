from lib.led_light import Led_Light
from lib.controller import PedestrianSubsystem
from lib.audio_notification import Audio_Notification
from lib.pedestrian_button import PedestrianButton
from time import sleep, time

red = Led_Light(19, True, True)
green = Led_Light(17, False, True)
button = PedestrianButton(22, True)
buzzer = Audio_Notification(27, True)

pedestrian = PedestrianSubsystem(red, green, button, buzzer, True)


def Pedestrian_Button_Driver():
    print("Testing Pedestrian system in 5 seconds")
    sleep(5)

    print("Testing show_stop, PASS if RED on, GREEN off")
    pedestrian.show_stop()
    sleep(5)

    print("Testing show_walk, PASS if GREEN on, RED off")
    pedestrian.show_walk()
    sleep(5)

    warning_start = time()
    while time() - warning_start < 10:
        pedestrian.show_warning()
        sleep(1)
    print("Pass if: Ped Red FLASHING, Ped Green OFF & Buzzer OFF")

    print("Testing show_warning, PASS if RED flash, BUZZER beep, GREEN off")
    for _ in range(10):
        pedestrian.show_warning()
        sleep(1)
        print("Show_warning test")
    sleep(5)

    print("Testing button, press within 5 seconds")
    sleep(5)
    if pedestrian.is_button_pressed():
        print("PASS: button detected")
    else:
        print("FAIL: Button not detected")
    sleep(5)

    print("Testing reset button, DO NOT PRESS BUTTON")
    sleep(5)
    pedestrian.reset_button()
    if pedestrian.is_button_pressed() is False:
        print("PASS: button_state = False")
    elif pedestrian.is_button_pressed() is True:
        print("FAIL: button_state = True")
    sleep(5)

    print("Test Complete")


Pedestrian_Button_Driver()
