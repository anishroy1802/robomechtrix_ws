#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

disToObstacle= 0.50 #50 cms threshold

def callback(message):

    # if dt.ranges[0]>disToObstacle and dt.ranges[60]>disToObstacle and dt.ranges[359]>disToObstacle: # Checks if there are obstacles in front and 150 degrees left and right 
									 
    #     move.linear.x = 1.50# go forward 
    #     move.angular.z = 0.00 # do not rotate 
    # else:
    #     move.linear.x = -0.15 # move slightly backwards
    #     move.angular.z = 1.00 # rotate counter-clockwise
    #     if dt.ranges[0]>disToObstacle and dt.ranges[60]>disToObstacle and dt.ranges[359]>disToObstacle:
    #         move.linear.x = 1.50
    #         move.angular.z = 0.00

    range={
        "right" : min(min(message.ranges[0:239]) , 2),
        "center" : min(min(message.ranges[240:479]) , 2),
        "left" : min(min(message.ranges[480:719]) , 2)
    }

    if ( range["right"] >disToObstacle  and range["center"] > disToObstacle and range["left"] >disToObstacle):
        case = 'NO OBSTACLE!'
        move.linear.x=0.6
        move.angular.z=0
    elif ( range["right"] > disToObstacle  and range["center"] < disToObstacle and range["left"] > disToObstacle ):
        case = 'OBSTACLE CENTER!'
        move.linear.x=0
        move.angular.z=-0.5
    elif ( range["right"] < disToObstacle  and range["center"] > disToObstacle and range["left"] > disToObstacle ):
        case = 'OBSTACLE RIGHT!'
        move.linear.x=0
        move.angular.z=0.5
    elif ( range["right"] > disToObstacle  and range["center"] > disToObstacle and range["left"] < disToObstacle ):
        case = 'OBSTACLE LEFT!'
        move.linear.x=0
        move.angular.z=-0.5
    elif ( range["right"] < disToObstacle  and range["center"] > disToObstacle and range["left"] < disToObstacle ):
        case = 'OBSTACLE RIGHT AND LEFT!'
        move.linear.x=0.6
        move.angular.z=0
    elif ( range["right"] > disToObstacle  and range["center"] < disToObstacle and range["left"] < disToObstacle ):
        case = 'OBSTACLE CENTER AND LEFT!'
        move.linear.x=0
        move.angular.z=-0.5
    elif ( range["right"] < disToObstacle  and range["center"] < disToObstacle and range["left"] > disToObstacle ):
        case = 'OBSTACLE CENTER AND RIGHT!'
        move.linear.x=0
        move.angular.z=0.5
    elif ( range["right"] < disToObstacle  and range["center"] < disToObstacle and range["left"] < 1 ):
        case = 'OBSTACLE AHEAD!'
        move.linear.x=0
        move.angular.z=0.8


    pub.publish(move) # publish the move object


rospy.init_node('avoidance-1')
sub = rospy.Subscriber('/scan', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
rate = rospy.Rate(5)
move = Twist()

rospy.spin()