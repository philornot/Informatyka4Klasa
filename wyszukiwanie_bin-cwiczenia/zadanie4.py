"""
Zadanie 4. Znajdź maksymalną długość kawałków (klasyczne zadanie „cięcie desek”)

Dane: Masz n desek o długościach L[i] i chcesz je pociąć tak, by uzyskać co najmniej k kawałków o tej samej długości d.
Wyjście: maksymalne całkowite d, takie, że można uzyskać co najmniej k kawałków.

Deski można ciąć dowolnie, ale nie można sklejać.

Przykład: dla L = [10, 15, 20]; k = 7, oczekiwany output to 5
"""


def potnij_na_kawalki(dlugosc_kawalka, deski):
    kawalki = 0
    for dlugosc_deski in deski:
        kawalki += (dlugosc_deski // dlugosc_kawalka)
    return kawalki


def znajdz_maks_d(k, L=[10, 15, 20]):
    lewy = 1
    prawy = max(L)
    d_maks = 0

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        print(f'Zakres: [{lewy}...{prawy}], srodek = {srodek}')
        if potnij_na_kawalki(srodek, L) >= k:
            d_maks = srodek
            lewy = srodek + 1  # przesuń zakres w prawo
        else:
            prawy = srodek - 1  # przesuń zakres w lewo

    return d_maks


print(znajdz_maks_d(7))
