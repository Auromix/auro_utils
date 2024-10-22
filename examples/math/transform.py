import numpy as np

from auro_utils.math.transform import wxzy_to_xyzw
from auro_utils.math.transform import xyzw_to_wxyz
from auro_utils.math.transform import pose_to_position_and_orientation
from auro_utils.math.transform import position_and_orientation_to_pose

# Sample quaternion data for testing
quaternion_xyzw = [0.1, 0.2, 0.3, 0.4]  # [x, y, z, w]
quaternion_wxyz = [0.4, 0.1, 0.2, 0.3]  # [w, x, y, z]
position = [1.0, 2.0, 3.0]  # [x, y, z]
orientation = [0.1, 0.2, 0.3, 0.4]  # [x, y, z, w]


# Example functions for quaternion and pose operations
def example_convert_xyzw_to_wxyz():
    converted = xyzw_to_wxyz(quaternion_xyzw)
    print("Converted from XYZW to WXYZ:", converted)


def example_convert_wxyz_to_xyzw():
    converted = wxzy_to_xyzw(quaternion_wxyz)
    print("Converted from WXYZ to XYZW:", converted)


def example_position_and_orientation_to_pose():
    pose = position_and_orientation_to_pose(position, orientation)
    print("Combined position and orientation to pose:", pose)


def example_pose_to_position_and_orientation():
    pose = position_and_orientation_to_pose(position, orientation)
    position_out, orientation_out = pose_to_position_and_orientation(pose)
    print(
        "Extracted position and orientation from pose:", position_out, orientation_out
    )


# Execute the example functions
if __name__ == "__main__":
    example_convert_xyzw_to_wxyz()
    example_convert_wxyz_to_xyzw()
    example_position_and_orientation_to_pose()
    example_pose_to_position_and_orientation()
