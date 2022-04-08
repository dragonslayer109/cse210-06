from pyray import *
from keyboard_service import KeyboardService
from cast import Cast
from video_service import VideoService

class Director:
    """
    Controls the game play and executes acctions as needed till game 
    is closed   
    """
    def __init__(self):
        self._video_service = VideoService()
        self._keyboard_service = KeyboardService()
        self._pop = 10
        self._cast = Cast()

    def start_game(self):
        """
        Run the game loop till game closed
        """
        self._video_service.open_window()
        self.populate()
        while not window_should_close():
            self.update()
            self._video_service.first_buffer()
            self.draw_objects()
            self._video_service.second_buffer()
    
    def populate(self):
        self._cast.create_ship()
        self._cast.create_alien(self._pop)

    def draw_objects(self):
        actors = self._cast.get_all_actors()
        print(actors)
        self._video_service.display_flying_objects(actors)

    def update(self):
        self._keyboard_service.get_direction()
        check = self._keyboard_service.get_bullet()
        if check:
            self._cast.create_bullet()
        self.collision()

    def collision(self):
        """
        check for collisions
        """
        too_close = 0
        #run through all objects and check for collision
        for alien in self._cast._aliens:
            for bullet in self._cast._bullets:
                if bullet.alive and alien.alive:
                    #collision of bullet and alien
                    if (abs(bullet.position.x - alien.position.x) <= too_close and
                        abs(bullet.position.y - alien.position.y) <= too_close):
                        #update objects and score
                        bullet.hit()
                        alien.hit()
                        self.score += 5
            
            if self._cast._ship.alive and alien.alive:
                #collision of ship and alien
                if (abs(self._cast._ship.position.x - alien.position.x) <= too_close and
                        abs(self._cast._ship.position.y - alien.position.y) <= too_close):
                        #update objects and score
                        alien.hit()
                        self._cast._ship.hit()
                        self.score -= 5

    def removal(self):
        self._cast.remove_object()

    def score(self):
        pass
        #print(self._video_service.score) #Will be changed to a display on board later.

