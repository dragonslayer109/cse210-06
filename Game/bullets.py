import pyray
import constants
import random
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
        self._position = Point()
        self.alive = True
    
    def draw_bullet(self):
        """
        Draw the bullet on the screen
        """
        self._position.x = int(random.uniform(0, constants.MAX_X))
        self._position.y = int(random.uniform(10, 30))

        text = self._text
        x = self._position.x
        y = self._position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)

    def collision(self):
        """
        Called when collision is made with an alien.
        """
<<<<<<< HEAD

        self.alive = False
=======
        self.alive = False
        
    def draw_bullet(self):
        """
        Draw the bullets
        """
        text = self._text
        self._position.x = int(random.uniform(0, constants.MAX_X))
        self._position.y = int(random.uniform(10, 30))
        x = self._position.x
        y = self._position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)
>>>>>>> 77b0d741e4a7faee2a3e82a8be4b1f69c0ec7fbc
