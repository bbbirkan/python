import time
from machine import Pin
from time import sleep




p2= Pin(2,Pin.OUT,value=0)

for i in range(3):
    time.sleep(1)
    print("acik")
    p2.on()
    time.sleep(1)
    p2.off()
    print("kapali")
   

