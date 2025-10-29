def szukaj_parzystej(tab):
    n = len(tab)
    lewy = 0
    prawy = n - 1
    srodek = (lewy + prawy) // 2
    while True:
        if tab[srodek] % 2 == 0:
            prawy = srodek - 1
            srodek = (lewy + prawy) // 2
            if tab[lewy] % 2 == 0:
                return tab[lewy]
        else:
            lewy = srodek + 1
            srodek = (lewy + prawy) // 2
            if tab[lewy] % 2 == 0:
                return tab[lewy - 1]


tab = [1, 23, 43, 31, 21, 47, 18, 22, 12, 6, 24]
tab2 = [1, 231, 14, 12, 44, 24, 12]
print(tab)
print(szukaj_parzystej(tab))
print(szukaj_parzystej(tab2))
