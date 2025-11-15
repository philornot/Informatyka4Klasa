def szukaj_parzystej(tab):
    n = len(tab)
    lewy = 0
    prawy = n - 1
    srodek = (lewy + prawy) // 2
    while True:
        if tab[srodek] % 2 == 0:
            prawy = srodek - 1
            if tab[srodek-1] % 2 != 0:
                return tab[srodek]
            srodek = (lewy + prawy) // 2

        else:
            lewy = srodek + 1
            srodek = (lewy + prawy) // 2


tab = [1, 23, 43, 31, 21, 47, 18, 22, 12, 6, 24]
tab2 = [1, 231, 14, 12, 44, 24, 12]
tab3 = [1, 231, 15, 13, 45, 23, 12]
print(tab, szukaj_parzystej(tab))
print(tab2, szukaj_parzystej(tab2))
print(tab3, szukaj_parzystej(tab3))
