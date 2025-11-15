"""
Zadanie 3: Ile liczb ≤ x — policz przez binary search

Masz posortowaną niemalejąco tablicę A.
Dla podanej wartości x określ, ile elementów tablicy jest ≤ x.
Nie wolno używać pętli liniowej (musi być logarytmicznie).

Przykład: dla A = [2, 2, 5, 7, 9, 9, 10]; x = 8; oczekiwany output to 4
"""


def ile_el_mniejszych_od_x(x, tab=[2, 2, 5, 7, 9, 9, 10]):
    lewy = 0
    prawy = len(tab)

    while lewy < prawy:
        print(f'Zakres: {tab[lewy:prawy]}')
        srodek = (lewy + prawy) // 2
        if tab[srodek] <= x:
            lewy = srodek + 1
        else:
            prawy = srodek

    return prawy


print("naciśnij enter żeby zakończyć program")
while True:
    x = input(f"x=")
    if x == "":
        break
    else:
        print(ile_el_mniejszych_od_x(int(x)), end="\n\n")