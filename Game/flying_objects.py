import pyray
from point import Point

class Flying_Objects():
    """
    Starting point of the object
    Velocity of the object moving
    """
    def __init__(self):
        self._position = Point()
        self.alive = True

    def draw(self):
        """
        Draw the flying object
        """
        text = self._text
        x = self._position.x
        y = self._position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)
   
    def update(self):
        pass

    def hit(self):
        """
        Called when collision is made with a bullet.
        """

        self.alive = False