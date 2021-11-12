# Create class named Music that receives title, artist and lyrics upon initialization.
# The class should also have methods print_info() and play(). The print_info() method
# should return the following:
# 'This is "{title}" from "{artist}"'. The play() method should return the lyrics.
# Submit only the class in the judge system. Test your code with your own examples.

class Music:

    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

song = Music(title="Can`t Go Wrong", artist="Wiley", lyrics="eskimo dance")
print(song.print_info())
print(song.play())
