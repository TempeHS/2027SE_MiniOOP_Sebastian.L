from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    """Simple class to turn an LED off and on a Raspberry Pi Pico

    Inherits from machine.Pin and provides methods to turn the LED on, off and flash it.

    Args:
        pin (int): The GPIO pin number to which the LED is connected.
        flashing (bool, optional): If True, enables flashing mode. Defaults to False.
        debug (bool, optional): If True, enables debug output. Defaults to False.

    Attributes:
        led_light_state (int): Property to get or set the LED state (1 for off, 0 for on).
        _last_toggle_time (float): Timestamp of the last toggle, used for flashing.

    Methods:
        flash():
            Toggles the LED state every 0.5 seconds if flashing is enabled.
    """

    def __init__(self, pin, flashing=False, debug=False):
        """Initializes the LED light.

        Args:
            pin (int): The GPIO pin number to which the LED is connected.
            flashing (bool, optional): If True, enables flashing mode. Defaults to False.
            debug (bool, optional): If True, enables debug output. Defaults to False.
        """

        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.led_light_state
        self._last_toggle_time = time()

    @property
    def led_light_state(self):
        """Gets the current state of the LED.

        Returns:
            int: The current state of the LED (1 for off, 0 for on).
        """

        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        """Sets the state of the LED.

        Args:
            value (int): The desired state of the LED (1 for off, 0 for on).

        Raises:
            ValueError: If the value is not 0 or 1.
        """
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        """Flashes the LED.

        Toggles the LED state every 0.5 seconds if flashing mode is enabled.

        Returns:
            None
        """

        now = time()
        if self.__flashing and now - self._last_toggle_time >= 0.5:
            self.toggle()
            self._last_toggle_time = now
