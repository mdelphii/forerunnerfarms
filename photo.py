import time  #import the time library
import os # import the os library

print 'Script Running!!'  # Print a message to let the user know that the scrip is running

x = 0 # set a counter variable x to zero
number_of_pictures = 1 #
for x in range (number_of_pictures): #while x is withing the range of number of pictures run the loop
    print 'Top Camera' #smile
    # os.system('fswebcam -d /dev/video0 -r 1280x1024 -S 10 --rotate 270 --save /home/pi/Pictures/GerminateCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
    print 'Bottom Camera'
    os.system('fswebcam -d /dev/video1  -r 1920x1080 -S 10 --rotate 180 --save /home/pi/Pictures/GrowCamera_%d%b%Y_%H%M%Sjpg' ) # us fswebcam to take a picture and name it using the current time
    print ' Picture taken'

