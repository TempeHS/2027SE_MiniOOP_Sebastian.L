from machine import Pin
from time


class Pedestrian(Pin):
    """Sub class inherits the super "pin" class implements pedestrian__button which gets input to display pedestrian status

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
        """Initializes the Pedestrian button.

        Args:
            pin (int): The GPIO pin number to which the LED is connected.
            flashing (bool, optional): If True, enables flashing mode. Defaults to False.
            debug (bool, optional): If True, enables debug output. Defaults to False.
        """

        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0
        self.__flashing = flashing
        self.__pedestrian_waiting = False
        # Set up interrupt on rising edge
        self.irq(trigger=pin.IRQ_RISING, handler=self.callback)

    def button_state(self, value=None):
        if value is None:
            # Getter
            if self.__debug:
                print(
                    f"Button connected to pin {self.__pin} os {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
                )
            return self.__pedestrian_waiting
        else:
            # Setter
            self.__pedestrian_waiting = bool(
                value
            )  # Convert to boolean to ensure the proper type
            if self.__debug:
                print(
                    f"Button state on Pin {self.__pin} set to {self.__pedestrian_waiting}"
                )

    def callback(self, pin):
        current_time = tick_ms()  # Get the current time in milliseconds
        if ticks_diff(current__time, self.__last_pressed) > 200:  # 200ms
            self.__last_pressed
            self.__pedestrian_waiting
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
