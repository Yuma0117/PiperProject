#!/usr/bin/env python

import RPi.GPIO as GPIO
import distance
import time
import subprocess
import boto3
import upload

def destory():
   GPIO.cleanup()

def loop():
    count = 0
    while True:
       d = distance.checkdist() 
       df = "%0.2f" %d #小数点第２位まで切り上げた距離 
       print (df)
       if float(df) <= 0.50:
          count += 1
          print (count)
          subprocess.run(["/home/pi/YO/camera.sh", "arguments"], shell=True)
          upload.s3_upload()
          subprocess.run(["/home/pi/YO/delete.sh", "arguments"], shell=True)
          time.sleep(15)
       else:
          time.sleep(1)

if __name__ == '__main__':
   try:
       loop()
   except KeyboardInterrupt:
       GPIO.cleanup()

