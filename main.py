import RPi.GPIO as GPIO
from time import sleep

dcmotor = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(dcmotor, GPIO.OUT)

pwm = GPIO.PWM(dcmotor, 100)

pwm.start(100)

for dc in range(100,-1,-1): 
  pwm.ChangeDutyCycle(dc)
  sleep(0.02)
