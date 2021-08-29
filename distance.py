# /usr/bin/python3

import RPi.GPIO as GPIO
import time

Trigger = 16
Echo = 18

def checkdist():
    GPIO.output(Trigger, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Trigger, GPIO.LOW)
    while not GPIO.input(Echo):
        pass
    t1 = time.time()
    while GPIO.input(Echo):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Trigger,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Echo,GPIO.IN)

#try:
#    count = 0
#    while True:
#        d = checkdist() #距離を図る
#        df = "%0.2f" %d #小数点第２位まで切り上げた距離
#        print ('Distance: %s m' %df)
#        if float(df) <= 0.10:
#           count += 1
#           print (count)
#           import hello_world
#        else:
#           count += 0
#        if count == 30:
#           print ("Well Done !!finish!!")
           #import hello_world
#          time.sleep(5)
#           count = 0
#        time.sleep(2)

#except KeyboardInterrupt:
#   GPIO.cleanup()
#   print ('GPIO cleeanup and end!')
