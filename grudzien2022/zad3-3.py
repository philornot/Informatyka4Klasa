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


def sito(n):
    tab = [0] * (n + 1)

    i = 0
    while i <= n:
        tab[i] = i
        i += 1
    tab[1] = 0  # 1 nie jest ani pierwsza, ani zlozona

    i = 2
    while i <= n:
        if tab[i] == 0:
            i += 1
            continue
        x = i * i
        while x <= n:
            tab[x] = 0
            x += i
        i += 1

    return tab


def na_ile_spodobow(n):
    tab_sito = sito(n)
    licznik = 0
    i = 1
    while i <= n / 2:
        i += 1

        if i not in tab_sito:
            continue

        j = n - i
        if j in tab_sito:
            licznik += 1

    return licznik


liczby = wczytaj_dane(przyklad=True)
liczby_slownik = {}
maks = 0
min = 99999999999
min_liczba, maks_liczba = 0, 0
for liczba in liczby:
    if na_ile_spodobow(liczba) > maks:
        maks = na_ile_spodobow(liczba)
        maks_liczba = liczba
    if na_ile_spodobow(liczba) < min:
        min = na_ile_spodobow(liczba)
        min_liczba = liczba


print(maks_liczba, maks)
print(min_liczba, min)
