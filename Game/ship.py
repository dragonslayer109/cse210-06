import pyray
import constants
import random

from point import Point
from color import Color
from flying_objects import Flying_Objects

class Ship(Flying_Objects):
    
    def __init__(self):
        self._text = "<|>"
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point()

    
    def draw_ship(self):
        """
        Draw position of the ship on screen
        """
        text = self._text
        self._position.x = int(random.uniform(0, constants.MAX_X))
        self._position.y = int(random.uniform(10, 30))
        x = self._position.x
        y = self._position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)

    def update(self):
        """
        Update position of ship based on keys pressed (move functionality)
        """
        pass

    def hit(self):
        """
        Called once collision is made with alien
        """
        self.alive = False
        #print game over to screen