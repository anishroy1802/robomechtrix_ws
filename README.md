# ros-obstacle-avoidance


This repo contains a mobile robot that can be spawned on Gazebo and an algorithm for obstacle avoidance. The robot, if faced with an obstacle at a distance less than 50 centimetres, turns and moves in the direction having maximum LiDAR Scan.
## Dependencies for the packagec

```
Xacro - sudo apt-get install ros-<version>-xacro
Gazebo - sudo apt-get install ros-<version>-gazebo-ros
```

To clone, build and run the ROS package
```
git clone https://github.com/anishroy1802/robomechtrix_ws.git
cd robomechtrix_ws
catkin_make
source devel/setup.bash
roslaunch trixy world.launch
```
In a new terminal window:
```
rosrun new_pack moveit.py
```
To verify correctness of the algorithm, the node containing the code for obstacle avoidance can be launched with the turtlebot model with the Gazebo Stage_4 map as well. 
