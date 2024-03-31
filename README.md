## 一个简单的双臂机器人抓取教程！
## A simple tutorial on dual arm robot pick & place!

(1)实验条件

(1)Experimental condition

Ubuntu20.04 + ros-noetic + moveit

(2)使用教程

(2) User Guide

①创建一个工作空间

① Create a workspace

```
mkdir ros_pp_ws
cd ros_pp_ws
```

②将代码下载到工作空间中

② Download code to workspace

```
git clone https://github.com/ppap36/dual_arm_pick-place.git
```

③编译工作空间

③ Compile workspace

```
catkin_make
```

④打开两个窗口，分别执行source 

④ Open two windows and perform source operations separately

```
source devel/setup.bash
```

⑤对于第一个窗口执行如下代码

⑤ Execute the following code for the first window
```
roslaunch test_gazebos_att bringup_moveit.launch
```
执行后就可以看到rviz和gazebo中的双机械臂

After execution, you can see the dual robotic arms in rviz and gazebo
![image](https://github.com/ppap36/dual_arm_pick-place/assets/108739132/73da675b-5ba8-48e7-9081-48fc92777b74)

⑥
之后，在另外一个窗口运行两个代码

Afterwards, run two codes in another window


物块生成代码

Block generation code
```
rosrun test_gazebos_att spawn_models.py
```
双臂抓取代码

Double arm grasping code
```
rosrun test_gazebos_att arms_pp.py
```
之后就可以看到两个机械臂进行抓取物块的操作啦

Afterwards, you can see two robotic arms performing the operation of grabbing blocks of material
![image](https://github.com/ppap36/dual_arm_pick-place/assets/108739132/6c672349-caaf-4682-ba3c-a3c3646c7236)

### Reference

本实验使用了gazebo抓取插件的代码：https://github.com/pal-robotics/gazebo_ros_link_attacher
