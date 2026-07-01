## Current Status

- Robot model can be visualized in RViz
- Robot can be spawned in Gazebo
- ros2_control hardware interface is loaded
- joint_state_broadcaster and diff_drive_controller are active
- Robot can move forward by publishing TwistStamped command

## Launch Gazebo Simulation

```bash
cd ~/ros_ws
source install/setup.bash
ros2 launch robot_description gazebo.launch.py


## 3. 验证控制系统

```md
## Check Controllers

```bash
ros2 control list_controllers
Expected:
joint_state_broadcaster active
diff_drive_controller active

ros2 control list_hardware_interfaces
Expected:
left/right wheel velocity command interfaces are claimed


## 4. 运动测试命令

```md
## Move Forward

```bash
ros2 topic pub /diff_drive_controller/cmd_vel geometry_msgs/msg/TwistStamped \
"{header: {frame_id: base_link}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}"

Stop Robot
ros2 topic pub --once /diff_drive_controller/cmd_vel geometry_msgs/msg/TwistStamped \
"{header: {frame_id: base_link}, twist: {linear: {x: 0.0}, angular: {z: 0.0}}}"