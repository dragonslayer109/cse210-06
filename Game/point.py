class Point:
    """A distance from a point of origin.

    Attr:
        _x: The horizontal distance from the point of origin.
        _y: The vertical distance from the point of origin.
    """
    
    def __init__(self):
        """Constructs a new Point.
        
        Args:
            x: The x (horizontal) value.
            y: The y (vertical) value.
        """

        self.x = 0
        self.y = 0


    def add(self, new):
        """Gets a new Point that is the sum of the new one and the given one.

        Args:
            new: The Point that needs to be added to the old one.

        Returns:
            Point: A new Point that is the sum of the new one and the given one.
        """

        x = self._x + new.get_x()
        y = self._y + new.get_y()

        return Point(x, y)

    def equals(self, new):
        """Checks whether the Point is the same as the given one.

        Args:
            new: The Point that the method needs to compare against the one one.

        Returns: 
            A value of "True" if the x and y are equal and a value of "False" if they aren't.
        """

        return self._x == new.get_x() and self._y == new.get_y()

    def scale(self, factor):
        """
        Scales the point by the given values.

        Args:
            factor: The value by which the method needs to scale the Point.
            
        Returns:
            Point: A new Point that has been scaled according to the values given.
        """

        return Point(self._x * factor, self._y * factor)