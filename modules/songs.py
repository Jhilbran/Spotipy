
from .media import Media
from .global_functions import list_item_selector
from .constants import canvas
import time
 
   
class Song(Media):
    """
        Songs Class for Spotipy, it contains all the song related methods
    """
    song_canvas = None
    album = None
    artist = None

    def __init__(self, duration, song_canvas, artist, album, **kwargs):
        super().__init__("song", duration)
        self.song_canvas = song_canvas
        self.artist = artist
        self.album = album
        self.user_new_attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
    