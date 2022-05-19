"""
User Class for Spotipy, it contains the user info (location, subscription type, country)
"""

class User():
    """docstring for User."""
    username = None
    location = None
    premium = False
    password = None
    email = None
    playlists = []

    def __init__(self, username, location, premium, password, email, **kwargs):
        self.username = username
        self.location = location
        self.premium = premium
        self.password = password
        self.email = email
        self.user_new_attributes = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def get_membership(self):
        return True if input('Enter Y if you are a premium user, enter N otherwise\n>').title()=="Y" else False
    
    def show_user_info(self):
        print(f'''User: {self.username}
              Location: {self.location}
              Premium: {self.premium}
              Email: {self.email}''') 
    