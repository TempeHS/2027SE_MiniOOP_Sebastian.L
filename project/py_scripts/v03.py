from lib.led_light import Led_Light
from time import sleep

red_light = Led_Light(3, True, True)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)

    def on(self):
        # method overriding polymorphism of the super class
        self.high()
        if self.__debug:
            print(f"LED connected to pin{self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the super class
        self.low()
        if self.__debug:
            print(f"LED connected to pin{self.__pin} is low")

    def toggle(self):
        # method overriding polypormhism of the super class
        if self.value() == 0:
            self.on
        elif self.value() == 1:
            self.off()


red_light = Led_Light(3)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
