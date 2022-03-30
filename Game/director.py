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
            self.draw_objects() # Should be ship
            self.draw_objects() # Should be aliens
            self.draw_objects() # Should be bullets
        self._video_service.close_window()
        #self._video_service.open_window()
        #while self._video_service.is_window_open():
        #self.draw_objects()
        #self._video_service.close_window()

    def draw_objects(self):
        self._video_service.display_flying_object()

    def update(self):
        pass
    def collision(self):
        pass
    def removal(self):
        pass
    def score(self):
        pass

