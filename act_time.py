import time
import datetime as dt
import sys

t_start = dt.datetime.now()

print (t_start)
print (t_start.hour)


while True:
    t_now = dt.datetime.now()
    print(t_now.hour)
    if t_now.hour > t_start.hour:
        print('Back to the future!!')
        sys.exit()
    else:
        print('Time to wait')
        
