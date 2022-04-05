import pyray
import constants
from aliens import Aliens
from ship import Ship
from bullets import Bullets

class VideoService:
    """The responsibility of this class is to display the game on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService.
        
        Args:
            debug: Checks to see whether the program needs to be run in debug mode.
        """
        self._aliens = []
        self._alien = Aliens()
        self.pop = 10
        self._ship = Ship()
        self._bullets = []
        self._bullet = Bullets()
        self._debug = debug
        self.score = 0

    def is_window_open(self):
        """Checks whether the window is open.

        Returns:
            A value of "True" if the window is open or "False" if the window is closed.
        """

        return not pyray.close_window()

    def open_window(self):
        """Opens the window.
        """

        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def first_buffer(self):
        """Prepares the screen for the next output of the game by clearing the screen and
        drawing the next output.
        """

        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        if self._debug == True:
            self._draw_grid()

    def second_buffer(self):
        """Prepares the screen after the end of the game's output.
        """ 

        pyray.end_drawing()

    def display_flying_object(self):
        """Displays the Flying Object on the screen.

        Args:
            flying_object: The Flying Object.
        """ 
        while self.pop > 0:
            self._aliens.append(self._alien)
            self.pop -= 1
        
        for alien in self._aliens:
            alien.draw()

        for bullet in self._bullets:
            bullet.draw()

        self._ship.draw()            
    
    def create_bullet(self):
        """
        Creat a bullet
        """
        self._bullets.append(self._bullet)

    def collision(self):
        """
        check for collisions
        """
        too_close = 0
        #run through all objects and check for collision
        for alien in self._aliens:
            for bullet in self._bullets:
                if bullet.alive and alien.alive:
                    #collision of bullet and alien
                    if (abs(bullet.position.x - alien.position.x) <= too_close and
                        abs(bullet.position.y - alien.position.y) <= too_close):
                        #update objects and score
                        bullet.hit()
                        alien.hit()
                        self.score += 5
            
            if self._ship.alive and alien.alive:
                #collision of ship and alien
                if (abs(self._ship.position.x - alien.position.x) <= too_close and
                        abs(self._ship.position.y - alien.position.y) <= too_close):
                        #update objects and score
                        alien.hit()
                        self._ship.hit()
                        self.score -= 5

    def _draw_grid(self):
        """
        Draws a grid on the screen and is used as a way to gather coordinates to determine the
        position of objects on the screen.
        """
        pass
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GREY)

        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GREY)

    def close_window(self):
        """Closes the window."""

        pyray.close_window()