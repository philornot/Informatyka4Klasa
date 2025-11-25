def funkcja(tab, liczba):
    lewy = 0  # to jest lewy indeks
    prawy = len(tab) - 1  # to jest prawy indeks
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if liczba == tab[srodek]:
            return srodek
        if liczba > tab[srodek]:
            lewy = srodek + 1
        elif liczby < tab[srodek]:
            prawy = srodek - 1

    return "Tej liczby nie ma w tablicy idioto"


# BEZ FUNKCJI:
tab = [1, 2, 4, 7, 8, 9, 11]  # najpierw jakieś napisy wejściowe
liczba = 3  # bo w funkcji mamy je w argumentach

# a kod jest dokładnie ten sam, z tym że zamieniamy return na print
lewy = 0
prawy = len(tab) - 1
while lewy <= prawy:
    srodek = (lewy + prawy) // 2
    if liczba == tab[srodek]:
        print(srodek)
        break  # no i tutaj musi być break bo inaczej ciągle będzie
        # spamować znalezionym środkiem
    if liczba > tab[srodek]:
        lewy = srodek + 1
    elif liczba < tab[srodek]:
        prawy = srodek - 1
# gdybyśmy zostawili print(-1) po prostu bez wcięcia to by ciągle
# printowało to -1, a tak printuje wtedy jak faktycznie ma printować
if liczba not in tab:
    print("Tej liczby nie ma w tablicy idioto")
