import os
from modules.songs import Song
from modules.playlist import Playlist
from modules.user import User
from modules.artist import Artist


song_directory = []
playlist_directory = []

def clear():
    '''Clears the screen'''
    os.system('cls')


def get_user():
    '''
    Get Username
    '''
    return input('Type your username\n>')

def get_bio():
    '''
    Gets the user's bio if input 'Y' is received
    '''
    add_bio = input('Do you want to add a bio? Y/N\n>').title()
    if add_bio == 'Y':
        bio = input('Type your bio\n>')
        return bio
    return None

def create_new_song(user):
    """Uses the Artist.load_song() method to create a son and append it to the load_directory

    Args:
        user (Artist Object): Artist who owns the song (the username will be added as the artist of the song)

    Returns:
        song_directory: dictionary with the appended song
    """
    song = user.load_song()
    song_directory.append(song)
    return song_directory

def create_new_song(user):
    """Uses the Artist.load_song() method to create a son and append it to the load_directory

    Args:
        user (Artist Object): Artist who owns the song (the username will be added as the artist of the song)

    Returns:
        song_directory: dictionary with the appended song
    """
    song = user.load_song()
    song_directory.append(song)
    return song_directory


artist_selection = input('Hello! Welcome to Spotipy, are you an Artist?Y/N\n>').title()


if artist_selection == 'Y':
    user1 = Artist(0,0,get_user(),"Barranquilla","pw","email@.com",artist=True,bio=get_bio())
    #cuando se inicializa el usuario se altera el orden de los args que se pasan, password muestra el email y premium muestra el password
    song1 = create_new_song(user1)
elif artist_selection == 'N':
    user1 = User(get_user(),"Barranquilla",User.get_membership(),"pw", "email@.com")

Song.play(song_directory[0])

song2 = create_new_song(user1)

playlist_directory.append(song1)
playlist_directory.append(song2)



clear()

