import numpy as np
import coords

"""
c0 is the april tag scanner
c1 is the center of the robot
offset is the offset of the april tag scan
"""
def transform_offset(c0, c1, offset):
    scanner_plus_offset = coords.Coords3D(c0.x + offset.x, c0.y + offset.y, c0.z + offset.z)
    return coords.Coords3D(scanner_plus_offset - c1.x, scanner_plus_offset - c1.y, scanner_plus_offset - c1.z)

"""
c0 is the april tag scanner
c1 is the center of the robot
distance is the distance of the april tag
"""
def transform_distance(c0, c1, distance):
    scanner_plus_distance = coords.Coords3D(c0.x + distance.x, c0.y + distance.y, c0.z + distance.z)
    return coords.Coords3D(scanner_plus_distance - c1.x, scanner_plus_distance - c1.y, scanner_plus_distance - c1.z)    

"""
distance is the relative distance of the april tag to the robot (obtained from transform_distance())
offset is the relative offset of the april tag to the robot (obtained from transform_offset())
"""
def calculate_relative_coords(distance, offset):
    return coords.Coords3D(distance.x + offset.x, distance.y + offset.y, distance.z + offset.z)

"""
tag_position_on_field is the position of the april tag on the field (obtained from april_tag enum)
tag_position_relative_to_robot is the position of the april tag relative to the robot (obtained from calculate_relative_coords())

This function returns the position of the robot on the field relative to the origin of the field.
"""
def calculate_robot_position(tag_position_on_field, tag_position_relative_to_robot):
    return coords.Coords3D(tag_position_on_field.x - tag_position_relative_to_robot.x, tag_position_on_field.y - tag_position_relative_to_robot.y, tag_position_on_field.z - tag_position_relative_to_robot.z)

"""
lidar_pos is the position of the lidar scanner on the robot
robot_center is the center of the robot
distance is the distance reading from the lidar scanner
"""
def transform_lidar_distance(lidar_pos, robot_center, distance):
    return distance - np.sqrt((lidar_pos.x - robot_center.x)**2 + (lidar_pos.y - robot_center.y)**2 + (lidar_pos.z - robot_center.z)**2)

"""
lidar_pos is the position of the lidar scanner relative to the front center of the robot
front_center is the front center of the robot
distance is the distance reading from the lidar scanner
"""
def transform_lidar_distance_to_front_center(lidar_pos, front_center, distance):
    return distance - np.sqrt((lidar_pos.x - front_center.x)**2 + (lidar_pos.y - front_center.y)**2 + (lidar_pos.z - front_center.z)**2)