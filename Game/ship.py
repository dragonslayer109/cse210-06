import pyray
import constants
import random

from point import Point
from color import Color
from flying_objects import Flying_Objects

class Ship(Flying_Objects):
    
    def __init__(self):
        self._text = "<|>"
        self._font_size = 20
        self._color = Color(255, 255, 255)
        self.position = Point()
        self.position.x = int(random.uniform(0, constants.MAX_X))
        self.position.y = int(random.uniform(560, constants.MAX_Y-20))
        self.lives = 3

    
    def draw(self):
        """
        Draw position of the ship on screen
        """
        text = self._text
        x = self.position.x
        y = self.position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)
        print(x)

    def update(self):
        """
        Update position of ship based on keys pressed (move functionality)
        """
        pass

    def move(self, movement):
        self.position.x += movement
        print(self.position.x)

    def hit(self):
        """
        Called once collision is made with alien
        """
        self.lives -= 1
        if self.lives <= 0:
            self.alive = False
        #print game over to screen