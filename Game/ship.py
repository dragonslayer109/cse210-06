import pyray
import constants
import random

from point import Point
from color import Color
from flying_objects import Flying_Objects

class Ship(Flying_Objects):
    
    def __init__(self):
        pass
        self._text = "🚀"
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point()

    
    def draw_ship(self):
        """
        Draw position of the ship on screen
        """
        self._position.x = random.uniform(0, constants.MAX_X)
        self._position.y = random.uniform(10, 30)
        color = self._color.rgb_value()
        pyray.draw_text(self._text, self._font_size, color, self._position.x, self._position.y)
    
    def update(self):
        """
        Update position of ship based on keys pressed
        """
        pass

    def hit(self):
        """
        Called once collision is made with alien
        """
        self.alive = False
        #print game over to screen