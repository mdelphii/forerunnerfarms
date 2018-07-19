import time  #import the time library
import os # import the os library
import serial 
from time import sleep
import sys
import datetime as dt
import sys

print 'Script Running!!'  # Print a message to let the user know that the scrip is running

ser = serial.Serial(
     port = '/dev/ttyACM1',
    baudrate =9600
    )

t_start = dt.datetime.now()

print (t_start)
print (t_start.min)


while True:
    t_now = dt.datetime.now()
    print(t_now.min)
    
    Hum = ser.readline()
    Temp = ser.readline()
    print(Hum)
    print(Temp)

    while t_now.min > (t_start.min+5):
        ser.write(b'1')
        ser.flush()
        print('MSG Sent-Lights On')
        sleep(0.5)
        os.system('fswebcam -r 320x240 -S 10 --save /home/pi/Pictures/%H%M%S.jpg') # us fswebcam to take a picture and name it using the current time
        print('Picture Taken')
        sleep(0.5)
        t_start = t_now.min

    while t_now.min <  (t_star.min + 5)
        ser.write(b'0')
        ser.flush()
        print('MSG Sent -Lights Off')
        sleep(0.5)
        os.system('fswebcam -r 320x240 -S 10 --save /home/pi/Pictures/%H%M%S.jpg') # us fswebcam to take a picture and name it using the current time
        print('Picture Taken')
        sleep(0.5)
            

    
#sys.exit()
    
    
    
   
    
    
