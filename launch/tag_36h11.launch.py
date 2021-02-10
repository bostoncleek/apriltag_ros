import os
import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from ament_index_python.packages import get_package_share_directory

print(os.path.join(get_package_share_directory("apriltag_ros"), "cfg", "tags_36h11.yaml"))

def generate_launch_description():
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/camera/color/image_raw"), ("/apriltag/camera_info", "/camera/color/camera_info")],
        parameters=[os.path.join(get_package_share_directory("apriltag_ros"), "cfg", "tags_36h11.yaml")])
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen'
    )

    return launch.LaunchDescription([container])