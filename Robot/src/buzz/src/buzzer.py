#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

def callback(data):
    print("buzzz")
    rospy.loginfo(data.data)
    l=int(data.data.strip())
    GPIO.output(21,1)
    print("starting buzzer")
    time.sleep(l)
    GPIO.output(21,0)
    print("stopping buzzer")

rospy.init_node('buzzer',anonymous=True)
rospy.Subscriber('/user',String,callback)
print("Starting")
rospy.spin()
