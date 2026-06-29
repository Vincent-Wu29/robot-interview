from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory("robot_description")

    xacro_file = os.path.join(
        pkg_path,
        "urdf",
        "simple_robot.urdf.xacro"
    )

    rviz_config = os.path.join(
        pkg_path,
        "rviz",
        "simple_robot.rviz"
    )

    robot_description = Command([
        "xacro ",
        xacro_file
    ])
    

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                "robot_description": robot_description
            }],
            output="screen"
        ),

        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", rviz_config],
            output="screen"
        )

    ])