# importok


from funcs_and_classes import offolo as off
from funcs_and_classes import szoveg_class as szov
from funcs_and_classes import lejatsz as lej


# dekas lista
lista = []

# a listába töltöm a szöveg/parancsokat

with open("csinal.txt", "r", encoding="utf8") as file:
    for sor in file:
        egy_sor = sor.strip().split(";")
        lista.append(szov.Szoveg(egy_sor[0], egy_sor[1]))


# a nem részleg
def no():
    lej.lejatsz("./mp3/sponge_effect.mp3")
    szov.time.sleep(3)
    lej.lejatsz("./mp3/song.mp3")

    for elem in lista:
        elem.kiir_vegrehajt()

    off.offolo()



    return 0


# cuni részleg

def yes():
    lej.lejatsz("./mp3/spongebob_sad.mp3")

    print("...............\n"
          "najova megusztad\n"
          "................\n"
          "megne lássalak megegyszer <333\n"
          "................\n"
          "**agressziv szarás hangok**\n"
          "................"
          )

    szov.time.sleep(7)
    return 0


if __name__ == '__main__':
    while True:

        lej.lejatsz("./mp3/elevator.mp3")

        ask = input("/////////////\n"
                    "Szerec? y/n: \n"
                    "/////////////\n\n")

        if ask.strip() == "y":
            yes()
        else:
            no()
