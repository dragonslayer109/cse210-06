import pyray
from point import Point


class KeyboardService:
    """This class detects the player's input on the keyboard.

    Attr:
        cell: The size of the current cell on the grid.
    """

    def __init__(self, cell = 1):
        """Constructs a new KeyboardService.
        
        Args:
            cell_size: The size of the current cell in the grid.
        """
        self._cell = cell

    def get_direction(self):
        """Gets the direction based on which keyboard keys the player presses.

        Returns:
            The direction.
        """
        direction_x = 0
        direction_y = 0
        
        if pyray.key_down(pyray.KEY_LEFT):
            direction_y = -1
        
        if pyray.key_down(pyray.KEY_RIGHT):
            direction_y = 1

        direction = Point(direction_x, direction_y)
        direction = direction.size(self._cell)
        
        return direction