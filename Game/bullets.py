import pyray
import constants
from flying_objects import Flying_Objects

class Bullets(Flying_Objects):
    """
    The visual representation of the bullets in the game. 
    Manages the appearance, position and velocity of the bullets.
    """

    def __init__(self):
        super().__init__()

        self._bullet = "🎇"

    def get_bullet(self):
        """Gets the visual representation of the bullet.
        
        Returns:
            The visual representation of the bullet.
        """

        return self._bullet
    
    def set_bullet(self, bullet):
        """Sets the appearance of the bullet.
        
        Args:
            bullet: The visual representation of the bullet.
        """

        self._bullet = bullet

    def collision(self):
        """
        Called when collision is made with an alien.
        """
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
