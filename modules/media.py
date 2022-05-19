import time

class Media():
    """
    Class for Media, it contains anything related to media (mp3) content. E.g. play content, count plays, like content, load albums or playlist
    """
    name = None
    likes = 0
    duration = 0
    plays = 0
    
    def __init__(self, media_type, duration=0):
        self.name = self.get_media_name(media_type)
        self.duration = duration
    
    def play(self):
        
        playtime = 0
        
        while playtime <= self.duration:
            print(f'Playing {self.name}')
            time.sleep(4)
            playtime += 4
        print('The reproduction has ended!')
        self.count_plays()
    
    def count_plays(self):
        self.plays += 1

    def show_media_name(self):
        print(f'{self.name}')

    def get_media_name(self, type):
        """Captures the name for the media item (song, album or playlist)

        Args:
            type (string): what will be shown on the 'enter the name of your {type}'
        """
        m_name = input(f'Enter the name of your {type}\n')
        print(f'{type} name loaded')
        return m_name