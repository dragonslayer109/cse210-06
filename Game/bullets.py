import pyray
import constants
import random
from ship import Ship
from flying_objects import Flying_Objects
from color import Color
from point import Point

class Bullets(Flying_Objects):
    """
    The visual representation of the bullets in the game. 
    Manages the appearance, position and velocity of the bullets.
    """

    def __init__(self):

        self._text = "*"
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._ship_position = Ship()
        self.alive = True
        self.move = Point()
    
    def draw(self):
        """
        Draw the bullet on the screen
        """

        text = self._text
        x = self._ship_position.position.x
        y = self._ship_position.position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)

    def update(self):
        self._ship_position.position.y -= (self.move.dy * 5)

    def collision(self):
        """
        Called when collision is made with an alien.
        """

        self.alive = False
