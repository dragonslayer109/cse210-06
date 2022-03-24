from flying_objects import Flying_Objects

class Ship(Flying_Objects):
    
    def __init__(self):
        pass
    
    def draw_ship(self):
        """
        Draw position of the ship on screen
        """
        pass
    
    def update(self):
        """
        Update position of ship based on keys pressed
        """
        pass

    def hit(self):
        """
        Called once collision is made with alien
        """
        self.alive = False
        #print game over to screen