
from .media import Media

class Album(Media):
    """
        Album Class for Spotipy, it contains all the Album related methods
    """
    artist = None
    
    
    def __init__(self, **kwargs):
        super().__init__("album")
        self.songs = []
        self.user_new_attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
