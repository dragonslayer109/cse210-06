
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
            pass
        self._video_service.close_window()

    def draw(self):
        self._video_service.clear_buffer()
        self._video_service.draw_
        self._video_service.draw_
        self._video_service.draw_
        self._video_service.draw_
        self._video_service.flush_buffer()


