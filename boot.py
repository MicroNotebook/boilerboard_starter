from boilerboard import Boilerboard
import time

b = Boilerboard()
b.screen.lcd.fill(1)
b.screen.lcd.show()

while True:
    p = b.irq.get_pressed_button()
    if p is not None:
        print(str(p))
    time.sleep(.1)

