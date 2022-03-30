import pyray
import constants
from flying_objects import Flying_Objects

class Aliens(Flying_Objects):
    """
    The visual representation of the aliens in the game. 
    Manages the appearance, position and velocity of the aliens.
    """

    def __init__(self):
        super().__init__()

        self._alien = "👽"

    def get_alien(self):
        """Gets the visual representation of the alien.
        
        Returns:
            The visual representation of the alien.
        """

        return self._alien
    
    def set_alien(self, alien):
        """Sets the visual appearance of the alien.
        
        Args:
            alien: The visual representation of the alien.
        """
        self._alien = alien

    def collision(self):
        """
        Called when collision is made with a bullet.
        """
        self.alive = False
        
    def draw_alien(self):
        """
        Draw aliens
        """
        text = self._text
        self._position.x = int(random.uniform(0, constants.MAX_X))
        self._position.y = int(random.uniform(10, 30))
        x = self._position.x
        y = self._position.y
        font_size = self._font_size
        color = self._color.rgb_value()
        pyray.draw_text(text, x, y, font_size, color)
