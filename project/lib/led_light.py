from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    """Simple class to turn an LED off and on a Raspberry Pi Pico
    Args

    """

    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.led_light_state
        self._last_toggle_time = time()

    @property
    def led_light_state(self):
        # Getter method
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        # setter method
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        # non-bloking flash : togglesled every 0.5 s fora given duration
        now = time()
        if self.__flashing and now - self._last_toggle_time >= 0.5:
            self.toggle()
            self._last_toggle_time = now
