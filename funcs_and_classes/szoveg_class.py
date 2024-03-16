import time
from PIL import Image
from funcs_and_classes import input_CC as inp

mega1 = Image.open(r"./png/mega.png")
mega2 = Image.open(r"./png/mega2.png")

class Szoveg:
    def __init__(self, a_szoveg, csinal):
        self.a_szoveg = a_szoveg
        self.csinal = csinal

    def kiir_vegrehajt(self):
        print("---------\n"
              f"{self.a_szoveg}\n"
              "---------")
        exec(self.csinal)
        time.sleep(3)

