import time  #import the time library
import os # import the os library
import serial 
from time import sleep
import sys
import datetime as dt
import sys

print 'Script Running!!'  # Print a message to let the user know that the scrip is running

ser = serial.Serial(port = '/dev/ttyACM0',baudrate =9600)

#t_start = dt.datetime.now()

#print (t_start)

file = open('ForerunnerFarmsData.csv','w')

file.write("Year,")
file.write("Month,")
file.write("Day,")
file.write("Hour,")
file.write("Minute,")
file.write("Sec,")
file.write("Temprature,")
file.write("Humidity,")

file.close()


t_On = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
t_Off = [22,23,0,1,2,3,4,5,6]


#t_On = [43,44,47,48]
#t_Off = [45,46]
state_switch = 0   

while True:
    t_now = dt.datetime.now()
    #print (t_start.minute)
    print(t_now.hour)
    print(t_now.year)


    
    Hum = ser.readline()
    Temp = ser.readline()
    print(Hum)
    print(Temp)

    file = open('ForerunnerFarmsData.csv','a')
    file.write(str(t_now.year) + ',')
    file.write(str(t_now.month) + ',')
    file.write(str(t_now.day) + ',')
    file.write(str(t_now.hour) + ',')
    file.write(str(t_now.minute) + ',')
    file.write(str(t_now.second) + ',')
    file.write(str(Temp) + ',')
    file.write(str(Hum))
    file.close()


    print('Waiting to switch')

    if t_now.hour in t_On:

        if state_switch == 0 :
            os.system('fswebcam -r 320x240 -S 10 --rotate 180 --save /home/pi/Pictures/%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
            print('Picture Taken')
            sleep(0.5)
        
        ser.write(b'1')
        ser.flush()
        print('MSG Sent-Lights On')
        sleep(0.5)
        state = ser.readline()
        print(state)
        state_switch = 1
        
       
        
    if t_now.hour in t_Off:

        if state_switch == 1 :
            os.system('fswebcam -r 320x240 -S 10 --rotate 180 --save /home/pi/Pictures/%d%b%Y_%H%M%S.jpg') # us fswebcam to take a picture and name it using the current time
            print('Picture Taken')
            sleep(0.5)
            
        ser.write(b'0')
        ser.flush()
        print('MSG Sent -Lights Off')
        sleep(0.5)
        state = ser.readline()
        print(state)
        state_switch = 0
       
