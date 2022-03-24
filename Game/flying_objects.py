import random
from point import Point

class Flying_Objects():
    """
    Starting point of the object
    Velocity of the object moving
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Point()
        self.alive = True

    def update(self):
        """
        Moves the objects
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy       