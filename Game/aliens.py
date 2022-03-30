import pyray
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

        self._text = "0^0"
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point()
        self.alive = True
    
    def draw_alien(self):
        """
        Draw the alien on the screen
        """

        self._position.x = int(random.uniform(0, constants.MAX_X))
        self._position.y = int(random.uniform(580, constants.MAX_Y))

        text = self._text
        x = self._position.x
        y = self._position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)

    def collision(self):
        """
        Called when collision is made with a bullet.
        """

        self.alive = False
