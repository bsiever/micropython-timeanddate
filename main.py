# Write your code here :-)
from microbit import *
import timeanddate

# h,m,s
timeanddate.setTime(0,0,0)
# m / d/ y
timeanddate.setDate(1,1,2021)

def displayTime():
    display.scroll(timeanddate.timestamp())

while True:
    if button_a.is_pressed():
        displayTime()
