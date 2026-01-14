def wczytaj_dane():
    with open('dane2_4.txt') as plik:
        dane_raw = plik.read()
    return dane_raw.split()


dane = wczytaj_dane()


def sprawdz_poprawnosc(wyrazenie):
    glebokosc = 0
    for znak in wyrazenie:
        if znak == '[':
            glebokosc += 1
        elif znak == ']':
            glebokosc -= 1
        else:
            return 0
    return glebokosc

for wyrazenie in dane:
    glebokosc = sprawdz_poprawnosc(wyrazenie)
    if glebokosc == 0:
        print('tak')
    else:
        print('nie')
