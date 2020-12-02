from machine import Pin


p2= Pin(2,Pin.OUT,value=0)
p2.on() # ilgili pine High yazar
p2.off() # ilgili pine Low yazar
help(Pin)