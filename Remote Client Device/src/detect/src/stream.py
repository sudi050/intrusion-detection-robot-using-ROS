#!/usr/bin/env python
import rospy
import cv2
import numpy as np
import base64
import os
from std_msgs.msg import String

# from playsound import playsound
i=0

# def alarm():
#     playsound('../Downloads/sound.mp3')

def callback(data):
    global i
    img=base64.b64decode(data.data)
    img=np.frombuffer(img,dtype=np.uint8)
    img=cv2.imdecode(buf=img,flags=1)
    cv2.imwrite("/detected/face"+str(i)+".jpg",img)
    cv2.imshow("Live Stream",img)
    cv2.waitKey(1)
    i+=1
        
if not os.path.isdir('/detected'):
    os.mkdir('/detected')
rospy.init_node('n2',anonymous=True)
rospy.Subscriber('stream',String,callback)
rospy.spin()
cv2.destroyAllWindows()