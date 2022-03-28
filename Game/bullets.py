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