class Coords2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
class Coords3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_2d(self):
        return Coords2D(self.x, self.y)

class SphereCoords:
    def __init__(self, distance, theta, phi):
        self.distance = distance
        self.theta = theta
        self.phi = phi