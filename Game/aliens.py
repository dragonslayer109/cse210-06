
import constants
import random

from flying_objects import Flying_Objects
from color import Color
from point import Point

class Aliens(Flying_Objects):
    """
    The visual representation of the aliens in the game. 
    Manages the appearance, position and velocity of the aliens.
    """

    def __init__(self):
        super().__init__()
        self._text = "0^0"
        self._font_size = 30
        self._color = Color(255, 255, 255)
        self._position = Point()
        self.alive = True
        self._position.x = int(random.uniform(0, constants.MAX_X))
        self._position.y = int(random.uniform(0, 20))
    

    def update(self):
        self._position.y += self._position.dy 


