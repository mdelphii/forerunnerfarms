import time  #import the time library
import os # import the os library
import serial
from time import sleep


print 'Script Running!!'  # Print a message to let the user know that the scrip is running

ser = serial.Serial(
    port = '/dev/ttyACM1',
    baudrate =9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1) # has to be a zero at the end

x = 0 # set a counter variable x to zero
number_of_pictures = 3 #
while True:
    #print 'Waiting for data...'
    state = ser.readline()
    print(state)




    for x in range (number_of_pictures): #while x is withing the range of number of pictures run the loop
        print 'Say Cheese' #smile
        os.system('fswebcam -r 320x240 -S 10 --save /home/pi/Pictures/%H%M%S.jpg') # us fswebcam to take a picture and name it using the current time
        print ' Picture taken'
        print x
        x=0
    sleep(10)
    
