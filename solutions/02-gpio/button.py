"""
Digital Electronics Lab
Board: FRDM-MCXN947
Example: Button input in MicroPython

Author: Tomas Fryza
Created: 2023-10-12
Last modified: 2026-01-30
"""

# Import the `Pin` class from the `machine` module to access hardware
from machine import Pin
import time

BTN_PIN = "P0_23"  # User button (check board schematic)
LED_PIN = "P0_27"  # Green LED (active-low)

DEBOUNCE_TIME_MS = 10


def main():
    """Main application entry point."""

    # Initialize button pin (with external pull-up)
    btn = Pin(BTN_PIN, Pin.IN)

    # Initialize LED pin (active-low)
    led = Pin(LED_PIN, Pin.OUT)
    led.on()

    print(f"Button pin info: {btn}")
    print(f"LED pin info: {led}")
    print("Press Ctrl+C to stop")

    try:
        while True:
            # Button is active-low with external pull-up
            if btn.value() == 0:
                led.off()
                print(f"Button {BTN_PIN} pressed")
                time.sleep_ms(DEBOUNCE_TIME_MS)

                # Wait here until the button is released (blocking)
                while btn.value() == 0:
                    time.sleep_ms(1)

                led.on()
                time.sleep_ms(DEBOUNCE_TIME_MS)

    except KeyboardInterrupt:
        # This part runs when Ctrl+C is pressed
        print("Program stopped. Exiting...")

        # Turn LED off before exit (active-low)
        led.on()


# Run this only when this file is the main program, not when it’s imported
if __name__ == "__main__":
    main()
