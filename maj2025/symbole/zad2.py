def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = 'symbole_przyklad.txt'
    else:
        plik = 'symbole.txt'
    with open(plik, 'r') as f:
        linie = f.read().split()
    return linie


# print(wczytaj_dane(przyklad=True))
napisy = wczytaj_dane(przyklad=True)

print(napisy[0][0])
print()
for napis in napisy:
    for i in range(len(napis)):
        if i + 2 < len(napis):
            if napis[i] == napis[i+1] == napis[i+2]:
                print(napis)