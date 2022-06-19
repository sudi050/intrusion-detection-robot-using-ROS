#!/usr/bin/env python3

from gpiozero import *
import rospy
import time

F=Robot(left=(6,5),right=(16,17))
B=Robot(left=(23,22),right=(24,25))

def forward(x):
    print("Forward")
    B.forward(1)
    F.forward(1)
    time.sleep(x)
    F.stop()
    B.stop()


def backward(x):
    print("Backward")
    B.backward(1)
    F.backward(1)
    time.sleep(x)
    F.stop()
    B.stop()

def turn_right():
    print("turn_right")
    B.left(1)
    F.left(1)
    time.sleep(0.9)
    F.stop()
    B.stop()

def turn_left():
    print("turn_left")
    B.right(1)
    F.right(1)
    time.sleep(1.2)
    F.stop()
    B.stop()

F.stop()
B.stop()

OPT=input("Enter 1 for remote control or 2 for predefined path:")
if OPT=="1":
    e='z'
    print("Move with W,A,S,D keys")
    while e!='e':
        e=input()
        if e=="w":
            forward(1)
        elif e=="s":
            backward(1)
        elif e=="d":
            turn_right()
        elif e=="a":
            turn_left()
        else:
            print("No way")
elif OPT=="2":
    while 1:
        forward(2)
        turn_left()

