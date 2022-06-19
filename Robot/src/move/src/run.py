#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

# from playsound import playsound


# def alarm():
#     playsound('../Downloads/sound.mp3')

def callback(data):
    rospy.loginfo(data.data)
    l=str(data.data)[1:-1]
    l=l.split('], [')
    for i in l:
        tmp=i.replace('[','').replace(']','')
        if (tmp.split(", ")[0].replace("'","") == "person" and float(tmp.split(", ")[1])>0.5):
            pass# alarm()
            
rospy.init_node('n2',anonymous=True)
rospy.Subscriber('detection',String,callback)
rospy.spin()
