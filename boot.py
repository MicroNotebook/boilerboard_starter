# Imports
import time
from boilerboard import Boilerboard

# Initialize boilerboard class
b = Boilerboard()

# Infinite loop
while True:

  # Get a pressed button
  button = b.irq.get_pressed_button()

  # Print button press if button is not None
  if button is not None:
    print(str(button))

  # Sleep to save battery/CPU
  time.sleep(.1)
