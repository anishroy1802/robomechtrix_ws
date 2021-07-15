#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

disToObstacle= 0.50 #50 cms threshold

def callback(dt):
    # print ('-------------------------------------------')
    # print ('Range data at 0 deg:   {}'.format(dt.ranges[0]))
    # print ('Range data at 75 deg:  {}'.format(dt.ranges[75]))
    # print ('Range data at 285 deg: {}'.format(dt.ranges[285]))

    max_scan= max(dt.ranges)
    print(max_scan)

    if(dt.ranges[0]> disToObstacle):
        move.linear.x = 0.50
        move.angular.z = 0
    else:
        move.linear.x = -0.10
        move.angular.z = 0.80
        if(dt.ranges[0]== max_scan):
            move.linear.x = 0.50
            move.angular.z = 0.0
    
    pub.publish(move) # publish the move object

    

rospy.init_node('avoidance')
sub = rospy.Subscriber('/scan', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
rate = rospy.Rate(5)
move = Twist()

rospy.spin()