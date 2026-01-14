def wczytaj_dane():
    with open('dane2_3.txt') as plik:
        dane_raw = plik.read()
    return dane_raw.split()


dane = wczytaj_dane()


def oblicz_glebokosc(wyrazenie):
    glebokosc = 0
    maks_glebokosc = 0
    for znak in wyrazenie:
        if znak == '[':
            glebokosc += 1
            if glebokosc > maks_glebokosc:
                maks_glebokosc = glebokosc
        elif znak == ']':
            glebokosc -= 1
        else:
            return 0
    return maks_glebokosc

for wyrazenie in dane:
    print(oblicz_glebokosc(wyrazenie))
