from lib.pedestrian_button import Pedestrian
from time import sleep

button = Pedestrian_Button(22, debug=True)

print("Please press and release the button within 5 seconds...")
pressed = False
for _ in range(50):
    if button.button_state:
        pressed = True
        break
    sleep(0.1)
if pressed:
    print("Button press detected:")
