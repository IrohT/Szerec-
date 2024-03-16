
from pygame import mixer


mixer.init()

def lejatsz(utvonal):
    mixer.music.stop()
    mixer.music.load(utvonal)
    mixer.music.play()
