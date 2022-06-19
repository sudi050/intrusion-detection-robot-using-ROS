#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

pub=rospy.Publisher('user',String,queue_size=10)
rospy.init_node('n2',anonymous=True)


def callback(data):
    rospy.loginfo(data.data)
    l=str(data.data)[1:-1]
    l=l.split('], [')
    for i in l:
        tmp=i.replace('[','').replace(']','')
        if tmp.split(", ")[0].replace("'","") == "person" and float(tmp.split(", ")[1])>0.5:
            pub.publish("3")
            return

rospy.Subscriber('detection',String,callback)
rospy.spin()

