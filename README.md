# Husky UGV Gesture Control
This repository is based on Unity and ROS to simulate hand gesture control on Husky mobile robot.

# Usage:
- Clone the offical Husky UGV repository:

  ```git clone https://github.com/husky/husky.git```
- Add RosBridge socket to this repository and rebuild your Workspace.
- ~~Add ROSConnect asset to Unity.~~ [Already added]
- Clone this repositroy:

  ```git clone https://github.com/YoushaaMurhij/Husky_UGV_Gesture_Control.git```
- Configure your IP and Port in Unity.
- ~~Add the required publishers and subscribers.~~[Done]
- Run Leapmotion Sensor or any hand gesture recognizer model.
- Run your project from ROS and Unity.

<p align="center">
  <img src="/husky.gif"> </img>
</p>

<p align="center">
  <img src="/Husky_unity.gif"> </img>
</p>

- Sample code to start with can be found in *Husky.py* file.

```python
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
    vel_hand_msg.angular.z = Husky_yaw_vel
    
    #rospy.sleep(0.0001)
    pub.publish(vel_hand_msg)
```


