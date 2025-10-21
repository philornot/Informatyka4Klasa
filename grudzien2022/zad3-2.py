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
    tab = [0] * N
    tab[0] = False

    for i in range(2, len(tab)):
        tab[i] = True

    for i in range(2, len(tab)):
        if tab[i] is True:
            j = i * i
            while j <= N:
                tab[j] = False
                j = i + i

    return tab


liczby = wczytaj_dane(przyklad=True)
print(liczby)
