
import time  #import the time library
import os # import the os library
import serial 
from time import sleep
import sys
import datetime as dt
import sys
import smtplib
import RPi.GPIO as GPIO


print 'Script Running!!'  # Print a message to let the user know that the scrip is running

#ser = serial.Serial(port = '/dev/ttyACM0',baudrate =9600)



#file = open('ForerunnerFarmsData.csv','w')

#file.write("Year,")
#file.write("Month,")
#file.write("Day,")
#file.write("Hour,")
#file.write("Minute,")
#file.write("Sec,")
#file.write("Temprature,")
#file.write("Humidity,")

#file.close()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

t_On = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
t_Off = [22,23,0,1,2,3,4,5,6]

sender = 'forerunnerfarms@gmail.com'
psw = 'Greenl0ngneck'
send_to = 'm.delphii@gmail.com'
content = 'A Picture of your plants has been taken!!'

midDay_pic = 0
endDay_pic = 0
state_switch = 0   

while True:
    t_now = dt.datetime.now()
    print(t_now.hour)
    print(t_now.year)


    
    #Hum = ser.readline()
    #Temp = ser.readline()
    #print(Hum)
    #print(Temp)

    #file = open('ForerunnerFarmsData.csv','a')
    #file.write(str(t_now.year) + ',')
    #file.write(str(t_now.month) + ',')
    #file.write(str(t_now.day) + ',')
    #file.write(str(t_now.hour) + ',')
    #file.write(str(t_now.minute) + ',')
    #file.write(str(t_now.second) + ',')
    #file.write(str(Temp) + ',')
    #file.write(str(Hum))
    #file.close()


    print('Waiting to switch')
    

    if t_now.hour in t_On:

        if state_switch == 0 :
            #print 'Top Camera' #smile
            #os.system('fswebcam -d /dev/video0 -r 1280x1024 -S 10 --rotate 270 --save /home/pi/Pictures/GerminateCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
            #print 'Bottom Camera'
            #os.system('fswebcam -d /dev/video1  -r 1920x1080 -S 10 --rotate 180 --save /home/pi/Pictures/GrowCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
            #print ' Picture taken'
            sleep(0.5)
            
			
        #ser.write(b'1')
        #ser.flush()
        print('MSG Sent-Lights On')
        GPIO.output(4,True)
        sleep(0.5)
        #state = ser.readline()
        #print(state)
        state_switch = 1
		
	if midDay_pic == 0:
		
		if t_now.hour == 12 :
			#print 'Top Camera' #smile
			#os.system('fswebcam -d /dev/video0 -r 1280x1024 -S 10 --rotate 270 --save /home/pi/Pictures/GerminateCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
			#print 'Bottom Camera'
			#os.system('fswebcam -d /dev/video1  -r 1920x1080 -S 10 --rotate 180 --save /home/pi/Pictures/GrowCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
			#print ' Picture taken'
			#print('Picture Taken')
			#sleep(0.5)
			
			mail = smtplib.SMTP('smtp.gmail.com:587')
			mail.ehlo()
			mail.starttls()
			mail.login(sender, psw)
			mail.sendmail(sender, send_to, content)
			mail.close()
			midDay_pic = 1
			
	if endDay_pic == 0:
		
		if t_now.hour == 21 :
			#print 'Top Camera' #smile
			#os.system('fswebcam -d /dev/video0 -r 1280x1024 -S 10 --rotate 270 --save /home/pi/Pictures/GerminateCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
			#print 'Bottom Camera'
			#os.system('fswebcam -d /dev/video1  -r 1920x1080 -S 10 --rotate 180 --save /home/pi/Pictures/GrowCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
			#print ' Picture taken'
			#print('Picture Taken')
			sleep(0.5)
			
			mail = smtplib.SMTP('smtp.gmail.com:587')
			mail.ehlo()
			mail.starttls()
			mail.login(sender, psw)
			mail.sendmail(sender, send_to, content)
			mail.close()
			endDay_pic = 1
   
        
    if t_now.hour in t_Off:

        if state_switch == 1 :
            #print 'Top Camera' #smile
            #os.system('fswebcam -d /dev/video0 -r 1280x1024 -S 10 --rotate 270 --save /home/pi/Pictures/GerminateCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
            #print 'Bottom Camera'
            #os.system('fswebcam -d /dev/video1  -r 1920x1080 -S 10 --rotate 180 --save /home/pi/Pictures/GrowCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
            #print ' Picture taken'
            #print('Picture Taken')
            sleep(0.5)
            
	GPIO.output(4,False)
        print('MSG Sent -Lights Off')
        sleep(0.5)
        state_switch = 0
        midDay_pic = 0
        endDay_pic = 0
        

       
