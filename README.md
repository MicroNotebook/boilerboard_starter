## Boilerboard Starter

> Note: If you haven't read the [guide](https://github.com/MicroNotebook/boilerboard-guides/blob/master/getting_started.ipynb) yet, you should read that first!

### Preface
Programming the hardware is as easy as writing python! This even means that you can access a repl, like normal python. However, because it is running on microcontrollers, we don't have the luxury of all python has to offer at our fingertips. Fortunately, in most use-cases, one won't find something that they can write in python that they can't write in micropython. If you need a good warmup or refresher on python, checkout [learnxinyminutes](https://learnxinyminutes.com/docs/python3/). Also, if you need to checkout what is available in micropython, checkout the [micropython docs](https://docs.micropython.org/en/latest/library/index.html).

### Intro
Interfacing with the boilerboard is easy. In this repository, you should find a file called [boilerboard.py](https://github.com/MicroNotebook/boilerboard_starter/edit/master/boilerboard.py). Inside is a bunch of python classes to help interface with the hardware. At the bottom, you should see a class called Boilerboard, which is the main one you'll be using. The main abilities that the board has are button presses and interacting with the screen (but the board also has GPIO pins that allow it to interface with external hardware).

### Uploading
Inorder to upload your code, you'll need ampy installed. Check the [esp8266 guide](https://github.com/MicroNotebook/guides/blob/master/esp8266.md#user-content-requirements) for instructions on how to install it. Once installed, you'll use ampy to upload files to the board. Examples of ampy commands can be found in the [boilerboard guide](https://github.com/MicroNotebook/boilerboard-guides/blob/master/getting_started.ipynb#Additional-ampy-Commands-to-Know). 

The basics of python running on the board are that on boot, micropython will execute the boot.py file, similar to if you just ran `python file.py`. You can upload multiple files other than boot.py and import them in boot.py using general python syntax (`from <filename> import <class>`) to spread out code.

### Examples

#### Tracking button presses
This example prints button presses to the serial connection.
> Note: `print()` in micropython's context prints to the serial connection. picocom on mac/linux, putty on windows
```python3
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
```

#### Writing to the screen
This updates the screen on each button press.
> Note: When using the screen, its important to know that whenever you modify the screen, call `screen.lcd.show()` to write all changes.
```python3
# Imports
import time
from boilerboard import Boilerboard

# Initialize boilerboard class
b = Boilerboard()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
START = 4
B = 5
A = 6

# Write text to the screen
b.screen.lcd.text('Button Press', 0, 0)
b.screen.lcd.show()

# Infinte loop
while True:
    # Get a pressed button
    button = b.irq.get_pressed_button()

    # Ignore None button press
    if button is None:
        continue

    # Clear screen
    b.screen.clear(0)

    # Write text to the screen
    b.screen.lcd.text('Button Press', 0, 0)

    # Write button to the screen
    if button == UP:
        b.screen.lcd.text('UP', 0, 20)
    elif button == RIGHT:
        b.screen.lcd.text('RIGHT', 0, 20)
    elif button == DOWN:
        b.screen.lcd.text('DOWN', 0, 20)
    elif button == LEFT:
        b.screen.lcd.text('LEFT', 0, 20)
    elif button == START:
        b.screen.lcd.text('START', 0, 20)
    elif button == B:
        b.screen.lcd.text('B', 0, 20)
    elif button == A:
        b.screen.lcd.text('A', 0, 20)

    b.screen.lcd.show()

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

### Docs
#### Buttons
Button presses using the boilerboard.py library use integers in python. [Check](https://github.com/MicroNotebook/boilerboard_starter/blob/master/boilerboard.py#L61) boilerboard.py in the Buttons class for the conversion. Note: const() is a micropython function to save memory, but doesn't matter that much.

#### The Screen
The screen is accessed by accessing your Boilerboard variable screen like:
```python3
b = Boilerboard()
# Clear the screen (0 is the color, which is blank)
b.screen.clear(0)
# To access the raw lcd, use screen.lcd
# This is the equivalend of the above line
b.screen.lcd.fill(0)
```

Some other functions that the screen object offer are `rect()`, `box()`, `hline()`, `vline()`, etc. Check out the class [here](https://github.com/MicroNotebook/boilerboard_starter/blob/master/boilerboard.py#L148).

The lcd object under screen offers direct acces to the screen, which has functions like `fill()`, `pixel()`, `show()`.

Remember to always call `show()` on the screen lcd to update any changes!
`b.screen.lcd.show()`

### Troubleshooting
* If you can't get micropython running on the board, e.g. picocom/putty into the board does not work, try reflashing micropython.
* If nothing is showing on the screen, make sure that you call `screen.lcd.show()` to flush changes.
