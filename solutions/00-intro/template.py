"""
Digital Electronics Lab
Board: FRDM-MCXN947
Example: MicroPython template can be interrupted using Ctrl+C

Author: Tomas Fryza
Created: 2023-09-21
Last modified: 2026-01-27
"""

import time


def main():
    """Main application entry point."""
    print("Press Ctrl+C to stop")

    try:
        while True:
            # Main loop
            time.sleep_ms(100)

    except KeyboardInterrupt:
        # This part runs when Ctrl+C is pressed
        print("Program stopped. Exiting...")

        # Optional cleanup code


# Run this only when this file is the main program, not when it’s imported
if __name__ == "__main__":
    main()
