
from .user import User
from .songs import Song
from .global_functions import list_item_selector, iterable_printer
from .constants import canvas

class Artist(User):
    artist = True
    total_songs = 0
    total_albums = 0
    bio = None
       
    """The Artist Class feeds fromt the User Class but it adds the Artist flag to load content"""
    
    def __init__(self, total_songs, total_albums, username, location, password, email, artist=True, bio=None, pic=None, premium=True, **kwargs):
        """init for the artist class. Uses the init from User

        Args:
            songs (int): number of songs under the artist
            albums (int): number of albums under the artist
            artist (bool, optional): Tag to differentiate between artists and regular users. Defaults to True.
            bio (str, optional): Short bio from the artist. Defaults to None.
            pic (str, optional): Banner picture. Defaults to None.
        """
        super().__init__(username, location, password, email, premium)
        self.artist = artist
        self.total_songs = total_songs
        self.total_albums = total_albums
        self.bio = bio
        self.pic = pic
        self.songs = []
        self.albums = []
        self.pic = [] 
        self.user_new_attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def load_song(self):
        """Gets Song name, duration and canvas using Song class methods
        """
        duration = int(input(f'Enter the duration of the song\n'))
        selected_canvas = list_item_selector(self, canvas)
        song_canvas = canvas[selected_canvas]
        album = input(f'Enter the album of the song\n')
        new_song = Song(duration,song_canvas,self.username, album)
        self.total_songs+=1
        self.total_albums+=1
        self.albums.append(new_song.album)
        self.songs.append(new_song.name)
        return new_song

    def load_album(self):
        duration = input(f'Enter the duration of the album\n')
        
    
    def load_song_to_album(self, user):
        if user.albums is True:
            print('This is the list of your albums')
            iterable_printer(self,user.albums)
            print('Input the number of the album you want to expand')
            album_number = list_item_selector(self,user.albums)
            print('Enter the information of the song you want to add:\n')
            