#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

disToObstacle= 0.50 #50 cms threshold

def callback(dt):
    max_scan= max(dt.ranges)
    print(max_scan)

    # if(dt.ranges[0]> disToObstacle):
    #     move.linear.x = 0.50
    #     move.angular.z = 0
    # else:
    #     move.linear.x = -0.10
    #     move.angular.z = 0.80
    #     if(dt.ranges[0]== max_scan):
    #         move.linear.x = 0.50
    #         move.angular.z = 0.0
    
    # pub.publish(move) # publish the move object

    right= dt.ranges[0]
    center= dt.ranges[240]
    left= dt.ranges[480]

    for i in range(0,240):
      if(dt.ranges[i]<right):
        right= dt.ranges[i]

    for i in range(0,240):
      if(dt.ranges[240+i]<center):
        center= dt.ranges[240+i]

    for i in range(0,240):
      if(dt.ranges[480+i]<left):
        left= dt.ranges[480+i]

    if(left>disToObstacle)and(right>disToObstacle)and(center>disToObstacle):
      print("No obstacle nearby!")
      move.linear.x= 0.50
      move.angular.z= 0.0

    else:
      if(center<disToObstacle):
        print("Obstacle in front")

        if(left<right)and(left>disToObstacle):
          print("Move cw")
          move.angular.z= -1.20
          move.linear.x= 0.0

          if(left>disToObstacle)and(right>disToObstacle)and(center>disToObstacle):

            print("No obstacle nearby!")
            move.linear.x= 0.50
            move.angular.z= 0.0


        elif(left>right)and(right>disToObstacle):
          print("Move ccw")
          move.angular.z= 1.20
          move.linear.x= 0.0

          if(left>disToObstacle)and(right>disToObstacle)and(center>disToObstacle):

            print("No obstacle nearby!")
            move.linear.x= 0.50
            move.angular.z= 0.0

        else:
          print("Move backwards")
          move.linear.x= - 0.50
          move.angular.z= -2.25

          if(left>disToObstacle)and(right>disToObstacle)and(center>disToObstacle):

            print("No obstacle nearby!")
            move.linear.x= 0.50
            move.angular.z= 0.0


    pub.publish(move)
            




      
        


rospy.init_node('avoidance')
sub = rospy.Subscriber('/scan', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
rate = rospy.Rate(5)
move = Twist()

rospy.spin()