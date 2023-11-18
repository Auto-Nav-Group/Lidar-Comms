import numpy as np
import pyurg

urg = pyurg.UrgDevice()
urg.connect()

data, timestamp = urg.capture() 

def sphere_to_cartesian(distance, theta, phi):
    x = distance * np.cos(theta) * np.cos(phi)
    y = distance * np.cos(theta) * np.sin(phi)
    z = distance * np.sin(theta)
    return x, y, z

""""
We have the position of the april tag scanner on the robot. We can use this to calculate the position of the robot
and to calculate relative positions of the april tag scanner and the origin of the field.
The lidar scans are relative distance to the lidar scanner. We can use this to calculate the position of the lidar scanner
relative to the center of the robot. We can then use this to calculate the position of the lidar scanner relative to the origin of the field.
With that, we can transform the distance data to cartesian coordinates.

Task list:
- Scan for april tags and get their position relative to the robot => done
- Transform the april tag position to the robot position (center of the robot) 
- Transform the robot position to the field position (origin of the field)
- Get lidar data from the lidar scanner
- Transform the distance data relative to the center of the robot
- Transform the distance data relative to the origin of the field
"""