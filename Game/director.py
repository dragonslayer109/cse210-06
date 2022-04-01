from pyray import *
from keyboard_service import KeyboardService
from video_service import VideoService

class Director:
    """
    Controls the game play and executes acctions as needed till game 
    is closed   
    """
    def __init__(self):
        self._video_service = VideoService()
        self._keyboard_service = KeyboardService()

    def start_game(self):
        """
        Run the game loop till game closed
        """
        self._video_service.open_window()

        while not window_should_close():
            self.update()
            self._video_service.first_buffer()
            self.draw_objects()
            self._video_service.second_buffer()

    def draw_objects(self):
        self._video_service.display_flying_object()

    def update(self):
        self._keyboard_service.get_direction()
        self.collision()

    def collision(self):
        self._video_service.collision()
        self.removal()
        self.score()

    def removal(self):
        for bullet in self._video_service._bullets:
            if not bullet.alive:
                self._video_service._bullets.remove(bullet)

        for alien in self._video_service._aliens:
            if not alien.alive:
                self._video_service._aliens.remove(alien)

    def score(self):
        print(self._video_service.score) #Will be changed to a display on board later.

