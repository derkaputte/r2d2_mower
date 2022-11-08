import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# Assuming you have a file called hls_lfcd_lds_driver/launch/hlds_laser.launch.py
my_launch_file = os.path.join(
    get_package_share_directory('hls_lfcd_lds_driver'),
    'launch',
    'hlds_laser.launch.py'
)

# Add this to your LaunchDescription
IncludeLaunchDescription(
    PythonLaunchDescriptionSource([my_launch_file])
)