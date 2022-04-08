from ship import Ship
from aliens import Aliens
from bullets import Bullets

class Cast():  
    
    def __init__(self):
        self._actors = []
        self._alien = Aliens()
        self._aliens = []
        self._ship = Ship()
        self._ships = []
        self._bullet = Bullets()
        self._bullets = []
    
    def create_alien(self, pop):
        """
        Create aliens
        """
        while pop > 0:
            self._aliens.extend(self._alien)
            pop -= 1   

    def create_ship(self):
        """
        Create a ship
        """
        self._ships.append(self._ship)

    def create_bullet(self):
        """
        Create a bullet
        """
        self._bullets.append(self._bullet)

    def get_all_actors(self):
        self._actors.extend(self._aliens)
        self._actors.extend(self._bullets)
        self._actors.extend(self._ship)
        return self._actors

    def remove_object(self):
        for bullet in self._bullets:
            if not bullet.alive:
                self._bullets.remove(bullet)

        for alien in self._aliens:
            if not alien.alive:
                self._aliens.remove(alien)