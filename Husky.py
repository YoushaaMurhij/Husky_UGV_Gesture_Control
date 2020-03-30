
import rospy 
import os, sys,inspect, thread, time

sys.path += ["/usr/lib/Leap", "../lib/x64", "../lib"]

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

from std_msgs.msg import Float64
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist

#initilizing a new node to catch the hand movemnt frames and and read its data
rospy.init_node('LM')

controller = Leap.Controller()
while(True):
    frame = controller.frame()
    Factor_LM_XY = -0.2
    Factor_LM_Z = -0.5
    #This factor represents a scaler to smooth the control movments

    #Extraxting the hand's center of mass (Palm) 6DOF data 
    hand = frame.hands[0]
    #Reading only the first hand from the available hands' list
    X = hand.palm_position.z
    Y = hand.palm_position.x
    Z = hand.palm_position.y
    pitch = hand.direction.pitch
    yaw   = hand.direction.yaw
    roll  = hand.palm_normal.roll
    #Aligning the robot's and han's system coordinate axis and scaling the control input
    Husky_x_vel = X * Factor_LM_XY   
    #Husky_y_vel = -1* Y * Factor_LM_XY # Y axis is in the opposite direction
    Husky_yaw_vel = yaw * Factor_LM_Z
    
    #robot.Pose()
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
    vel_hand_msg=Twist()
    vel_hand_msg.linear.x= Husky_x_vel
    vel_hand_msg.linear.y = 0
    vel_hand_msg.linear.z = 0
    vel_hand_msg.angular.x = 0
    vel_hand_msg.angular.y = 0
    vel_hand_msg.angular.z = Husky_yaw_vel
    
    #rospy.sleep(0.0001)
    #publising Twist msg every iteration..
    pub.publish(vel_hand_msg)
     
'''
def values(stdscr):
    stdscr.clear()
    #print '(w for forward, a for left, s for reverse, d for right,k for turning left,l for turning right and . to exit)' + '\n'

    keys=stdscr.getch()
    #s = raw_input(':- ')
    if keys == ord('w') or keys == curses.KEY_UP:
        twist.linear.x = 0.5 #* power
        twist.angular.z = 0.0
        twist.linear.y = 0.0

    elif keys == ord('s') or keys == curses.KEY_DOWN:
        twist.linear.x = -0.5 #* power
        twist.angular.z = 0.0
        twist.linear.y = 0.0

    elif keys == ord('a') or keys == curses.KEY_LEFT:
        twist.angular.z = 1.0 #* power
        twist.linear.x = twist.linear.y = 0.0
    elif keys == ord('d') or keys == curses.KEY_RIGHT:
        twist.angular.z = -1.0 #* power
        twist.linear.x = twist.linear.y = 0.0
    elif keys == ord('.') or keys == ord('x'):
        twist.angular.z = twist.linear.x = twist.linear.y = 0.0
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit()

    else:
        twist.linear.x = twist.linear.y = twist.angular.z = 0.0
        print 'Wrong command entered \n'

'''


