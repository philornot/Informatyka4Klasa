def wczytaj_dane(przyklad=False):
    if przyklad:
        plik = 'liczby_przyklad.txt'
    else:
        plik = 'liczby.txt'
    liczby = []
    with open(plik) as f:
        for linia in f.readlines():
            liczba = int(linia.strip())
            liczby.append(liczba)

    return liczby


def sito(N):
    tab = [False] * N

    for i in range(2, N):
        tab[i] = True

    for i in range(2, N):
        if tab[i]:
            j = i * i
            while j < N:
                tab[j] = False
                j = j + i

    return tab


liczby = wczytaj_dane(przyklad=True)
# print(liczby)
tab = sito(len(liczby))

licznik = 0
for x in range(len(tab)):
    if tab[x - 1]:
        licznik += 1

print(licznik)
