def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = 'symbole_przyklad.txt'
    else:
        plik = 'symbole.txt'
    with open(plik, 'r') as f:
        linie = f.read().split()
    return linie


def palindrom(napis):
    i = 1
    while i <= len(napis):
        if napis[i - 1] != napis[-i]:
            return False
        i += 1
    return True


napisy = wczytaj_dane(przyklad=False)
for napis in napisy:
    if palindrom(napis):
        print(napis)
