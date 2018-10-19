## Boilerboard Starter

> Note: If you haven't read the [guide](https://github.com/MicroNotebook/boilerboard-guides/blob/master/getting_started.ipynb) yet, you should read that first!

### Preface
Programming the hardware is as easy as writing python! This even means that you can access a repl, like normal python However, because it is running on microcontrollers, we don't have the luxury of all python has to offer at our fingertips. Fortunately, in most use-cases, one won't find something that they can write in python that they can't write in micropython. If you need a good warmup or refresher on python, checkout [learnxinyminutes](https://learnxinyminutes.com/docs/python3/). Also, if you need to checkout what is available in micropython, checkout the [micropython docs](https://docs.micropython.org/en/latest/library/index.html).

### Intro

Interfacing with the boilerboard is easy. In this repository, you should find a file called [boilerboard.py](https://github.com/MicroNotebook/boilerboard_starter/edit/master/boilerboard.py). Inside is a bunch of python classes to help interface with the hardware. At the bottom, you should see a class called Boilerboard, which is the main one you'll be using. The main abilities that the board has are button presses and interacting with the screen (but the board also has GPIO pins that allow it to interface with external hardware).

### Examples

#### Tracking button presses
```python3
# Imports
import time
from boilerboard import Boilerboard

# Initilize boilerboard class
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
```

#### Connecting to the internet
> Note: this doesn't use the boilerboard library, but you can integrate it if you want!
```python3
# Imports
import network

# Initialize network hardware
sta_if = network.WLAN(network.STA_IF)

# Connect
if not sta_if.isconnected():
  print('connecting to network...')
  # Activate network scanning
  sta_if.active(True)
  # Connect to the network (<essid> is the network name e.g. BoilerMake24 and <password> is the password)
  sta_if.connect('<essid>', '<password>')
  # Wait till connected
  while not sta_if.isconnected():
    pass
# Print network info
print('network config:', sta_if.ifconfig())
```

### Troubleshooting
* If you can't get micropython running on the board, e.g. picocom/putty into the board does not work, try reflashing micropython.
