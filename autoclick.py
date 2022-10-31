from time import sleep
from pynput.mouse import *

clicks = int(input("How many clicks? "))
seg = 3
mouse = Controller()

while seg>0:
    seg = seg-1
    sleep(1)
while clicks>0:
    clicks = clicks-1
    mouse.click(Button.left, 1)
    sleep(0.1)
    print('clicks',clicks)
