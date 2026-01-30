"""
Digital Electronics Lab
Board: FRDM-MCXN947
Example: LED blink in MicroPython

Author: Tomas Fryza
Created: 2023-09-21
Last modified: 2026-01-30
"""

# Import the `Pin` class from the `machine` module to access hardware
from machine import Pin
import time

LED_PIN = "P0_27"  # Green LED (active-low)
LED_ON_TIME_MS = 100
LED_OFF_TIME_MS = 900


def main():
    """Main application entry point."""

    # Initialize LED pin (active-low)
    led = Pin(LED_PIN, Pin.OUT)

    print(f"LED pin info: {led}")
    print("Press Ctrl+C to stop")

    try:
        while True:
            # LED ON (active-low)
            led.off()
            time.sleep_ms(LED_ON_TIME_MS)

            # LED OFF
            led.on()
            time.sleep_ms(LED_OFF_TIME_MS)
    
            # led.value(not led.value())
            # time.sleep_ms(500)

    except KeyboardInterrupt:
        # This part runs when Ctrl+C is pressed
        print("Program stopped. Exiting...")

        # Optional cleanup code
        # Turn LED off before exit (active-low)
        led.on()


# Run this only when this file is the main program, not when it’s imported
if __name__ == "__main__":
    main()
