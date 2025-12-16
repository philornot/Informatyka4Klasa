def czy_lustrzane(liczba1, liczba2):
    liczba1 = str(liczba1)
    liczba2 = str(liczba2)
    return liczba1[::-1] == liczba2


def lustro(liczba):
    liczba = str(liczba)
    return liczba[::-1]


def wczytaj_dane():
    plik = 'liczby.txt'
    with open(plik) as f:
        linie = f.read()
    return linie.split()


liczby = wczytaj_dane()

lustrzane = []
licznik_lustrzanych = 0
for i in range(len(liczby)):
    for j in range(len(liczby)):
        l1, l2 = liczby[i], liczby[j]
        if czy_lustrzane(l1, l2):
            licznik_lustrzanych += 1
            lustrzane.append((l1, l2))

print(f'jest {licznik_lustrzanych} lustrzanych par\n{lustrzane}')