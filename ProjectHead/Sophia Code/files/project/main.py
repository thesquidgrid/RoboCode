#!/usr/bin/env pybricks-micropython
#from pybricks.hubs import EV3Brick
#from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
 #                                InfraredSensor, UltrasonicSensor, GyroSensor)
#from pybricks.parameters import Port, Stop, Direction, Button, Color
#from pybricks.tools import wait, StopWatch, DataLog
#from pybricks.robotics import DriveBase
#from pybricks.media.ev3dev import SoundFile, ImageFile

# Modules to Import
#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.nxtdevices import UltrasonicSensor, TouchSensor, LightSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import time
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.BLACK, Color.BROWN]

# Objects to 
#light sensor to determine if goal is not guarded
#motors to drive


left = Motor(Port.B)
right = Motor(Port.A)
ultraSonic = UltrasonicSensor(Port.S3)
light = ColorSensor(Port.S2)
puck = Motor(Port.C)
robot_drive = DriveBase(left, right, 55.5, 104)




"""
robot_drive.straight(550) 
color = light.color

while(color==Color.WHITE):
    robot_drive.straight(20)#small amoubt
    color=light.color

 # get it a little behind the line
robot_drive.turn(-145)

color = light.color
while(color == Color.WHITE):
    robot_drive.turn(20)# turn a little bit to the left to get on track
"""



# Main control loop

colors = light.color()
print(colors)
goneLeft = False
goneRight = False

for cycle in range(100000):
    
    colors = light.color()
    
   
    # If the reflected light is too high turn left
    if colors in POSSIBLE_COLORS:
        if(goneLeft == True):
            robot_drive.drive(50, 10) # go right
            goneLeft = False
            goneRight = True
            
            print(colors)
        if(goneRight == True): 
            robot_drive.drive(40,-20) #go left
            goneRight = False
            goneLeft = True

        if(goneRight == False and goneLeft == False):
            robot_drive.drive(40,-20) # go left
            goneLeft = True
        print(colors)
        colors = light.color()
        

    # If the reflected light is too low turn right
    while colors == Color.BLACK:
        robot_drive.straight(30)
        colors = light.color()
        
        print(colors)
   


puckgone1 = False
while(puckgone1==False):
    if(ultraSonic.distance() == 200):
        puckgone1 = True
        puck.run_angle(10000,110,then=Stop.HOLD, wait=True)
        puck.run_angle(10000,-110,then=Stop.HOLD, wait=True)
    
colors = light.color()
for colors in POSSIBLE_COLORS:
    robot_drive.staright(-20)
    colors = light.color()
    