"""
Digital Electronics Lab
FRDM-MCXN947
LED blink example in MicroPython

Author: Tomas Fryza

Creation date: 2023-09-21
Last modified: 2026-01-27
"""

# Import the `Pin` class from the `machine` module to access hardware
from machine import Pin
import time

LED_ON_TIME_MS = 100
LED_OFF_TIME_MS = 900


def main():
    """Main application entry point."""

    # Initialize FRDM-MCXN947 red LED (active-low)
    led_r = Pin("P0_10", Pin.OUT)

    print(f"Pin info: {led_r}")
    print("Press Ctrl+C to stop")

    try:
        while True:
            # LED ON (active-low)
            led_r.off()
            time.sleep_ms(LED_ON_TIME_MS)

            # LED OFF
            led_r.on()
            time.sleep_ms(LED_OFF_TIME_MS)
    
            # led_r.value(not led_r.value())
            # time.sleep_ms(500)

    except KeyboardInterrupt:
        # This part runs when Ctrl+C is pressed
        print("Program stopped. Exiting...")

        # Optional cleanup code
        # Turn LED off before exit (active-low)
        led_r.on()


# Run this only when this file is the main program, not when it’s imported
if __name__ == "__main__":
    main()
