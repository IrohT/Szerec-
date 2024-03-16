
from ctypes import windll

def ScreenOFF():
    windll.user32.SendMessageW(65535, 274, 61808, 2)

def ScreenON():
    windll.user32.SendMessageW(65535, 274, 61808, -1)

