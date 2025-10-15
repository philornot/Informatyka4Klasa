n = 100
tab = [0] * n

i = 0
while i < n:
    tab[i] = i
    i += 1

i = 2
while i < n:
    if tab[i] == 0:
        continue
    x = i * i  # potęgowanie optymalizuje kod (zaczynamy od potęgi liczby pierwszej, wszystkie mniejsze zostały już skreślone przez mniejsze liczby pierwsze)
    # czyli dla i = 3, x = 9, później 12, 15... -> liczby podzielne przez 3 i < 2 (czyli 6) zostały już 'skreślone' przez dwójkę.
    # print(f'i={i}, x ={x}, n={n}')
    while x < n:
        tab[x] = 0
        x += i

    i += 1

for i in tab:
    if i != 0 and i != 1:
        print(i, end=' ')
