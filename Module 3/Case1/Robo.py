#A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT.
#The trace of Robot movement is as given following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after directions are steps.
#Write a program to compute the distance current position after sequence of movements.
#Hint: Use math module.

import math

Initial=[0,0]
action=[0,0]

while True:
     value =input("Enter the value to play, eg. UP5,DW3,LT2,RT2 | EX to exit")
     value=list(value)
     v=''.join(value[0:2])
     if v == "UP":
          action[1]=action[1]+int(value[2])
          print(action)
     elif v=="DW":
          action[1]=action[1]-int(value[2])
          print(action)
     elif v =="LT":
          action[0]=action[0]-int(value[2])
          print(action)
     elif v=="RT":
          action[0]=action[0]+int(value[2])
          print(action)
     elif v=="EX":
          dist=math.sqrt((action[0]-Initial[0])**2+(action[1]-Initial[1])**2)
          print(dist)
          break
