import time  #import the time library
import os # import the os library
import serial
from time import sleep
import sys


print 'Script Running!!'  # Print a message to let the user know that the scrip is running

ser = serial.Serial(
     port = '/dev/ttyACM1',
    baudrate =9600
    )

    # has to be a zero at the end
state = ser.readline()
print(state)
ser.write(b'1')
sleep(0.5)
os.system('fswebcam -r 640x480 -S 10 --save /home/pi/Pictures/%H%M%S.jpg') # us fswebcam to take a picture and name it using the current time
print('Picture Taken')
