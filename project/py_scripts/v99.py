from lib.led_light import Led_Light
from lib.controller import Controller
from lib.audio_notification import Audio_Notification
from lib.pedestrian_button import PedestrianButton
from time import sleep, time

ped_red = Led_Light(19, True, False)
ped_green = Led_Light(17, False, False)
button = PedestrianButton(22, debug=False)
buzzer = Audio_Notification(27, True)
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)

controller = Controller(
    ped_red,
    ped_green,
    led_traffic_red,
    led_traffic_amber,
    led_traffic_green,
    button,
    buzzer,
    True,
)

while True:
    controller.update()
    sleep(0.1)
