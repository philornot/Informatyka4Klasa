n = 67  # największa liczba w tablicy do posortowania
zakres = n + 1
tab = [0] * zakres  # jak zakres od 0 - 9 liczb czyli 10 elementów
# w tej tablicy będziemy zapisywać wystąpienia

tab_do_posortowania = [3, 2, 5, 67, 7, 3, 8, 2]
tab_posortowana = []

for i in range(zakres):
    for liczba in tab_do_posortowania:
        if liczba == i:
            tab[i] += 1

for j in range(zakres):
    if tab[j] == 0:
        continue
    for k in range(tab[j]):
        tab_posortowana.append(j)
        print(j, end=' ')

print(tab_posortowana)
