# Basic code for servo control using manual PWM
# Set PWM period = 20 ms
# 1 ms ON = full CW = 5% duty cycle
# 2 ms ON = full CCW = 10% duty cycle

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 18
GPIO.setup(pwmPin, GPIO.OUT)
# set min & max % duty cycles (5 and 10 are default values, but play
# around to find optimum values for your motor)

dcMin = 2
dcMax = 13

pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(0)
t = 0.05

try:
  while True:
    for dc in range(dcMin,dcMax):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(t)
    for dc in range(dcMax, dcMin, -1):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(t)

except KeyboardInterrupt:
  print("bye")

GPIO.cleanup()