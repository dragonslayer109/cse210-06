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

        return self._rock
    
    def set_rock(self, alien):
        """Sets the visual appearance of the alien.
        
        Args:
            alien: The visual representation of the alien.
        """
        self._alien = alien