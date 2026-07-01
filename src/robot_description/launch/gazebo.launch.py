from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
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

    world_file = os.path.join(
        pkg_path,
        "worlds",
        "empty.sdf"
    )

    robot_description = Command([
        "xacro ",
        xacro_file
    ])

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_file],
            output="screen"
        ),

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                "use_sim_time": True,
                "robot_description": robot_description
            }],
            output="screen"
        ),

        Node(
            package="ros_gz_sim",
            executable="create",
            arguments=[
                "-topic", "robot_description",
                "-name", "simple_robot",
                "-x", "0",
                "-y", "0",
                "-z", "0.0"
            ],
            output="screen"
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=[
                "joint_state_broadcaster",
                "--controller-manager",
                "/controller_manager"
            ],
            output="screen"
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=[
                "diff_drive_controller",
                "--controller-manager",
                "/controller_manager"
            ],
            output="screen"
        )
    ])