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
        while self._video_service.is_window_open():
<<<<<<< HEAD
            self.draw_objects() # Should be ship
            self.draw_objects() # Should be aliens
            self.draw_objects() # Should be bullets
        self._video_service.close_window()
        #self._video_service.open_window()
        #while self._video_service.is_window_open():
        #self.draw_objects()
        #self._video_service.close_window()
=======
            self.draw_objects()
            self.update()
            
        self._video_service.close_window()
>>>>>>> 77b0d741e4a7faee2a3e82a8be4b1f69c0ec7fbc

    def draw_objects(self):
        self._video_service.display_flying_object()

    def update(self):
        self.collision()

    def collision(self):
        self.removal()
        self.score()

    def removal(self):
        pass
    def score(self):
        pass

