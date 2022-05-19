from .media import Media
from .global_functions import list_item_selector
from .constants import canvas
import time
 
   
class Playlist(Media):
    """
        Playlist Class for Spotipy, it contains all the playlist related methods
    """    
    def __init__(self, artist, **kwargs):
        super().__init__("album")
        self.songs = []
        self.user_new_attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)