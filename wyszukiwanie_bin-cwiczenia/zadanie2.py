"""
Zadanie 2: Pierwsza pozycja ≥ x w posortowanej tablicy

Dana jest rosnąca tablica liczb całkowitych A[0..n−1].
Dla danego x zwróć indeks pierwszej liczby większej lub równej x.
Jeśli nie istnieje, wypisz −1.

Przykład: dla A = [1, 3, 3, 10, 14, 18]; x = 3; oczekiwany output to 1.
"""


def pierwsza_poz(x, A=[1, 3, 3, 10, 14, 18]):
    if x > A[-1]:
        return -1

    lewy = 0
    prawy = len(A)
    srodek = (lewy + prawy) // 2

    while lewy < prawy:
        # print(f'Zakres: {A[lewy:prawy]}')
        if A[srodek] >= x:
            prawy = srodek
        else:
            lewy = srodek + 1

        srodek = (lewy + prawy) // 2

    return srodek


print("naciśnij enter żeby zakończyć program")
while True:
    x = input(f"x=")
    if x == "":
        break
    else:
        print(pierwsza_poz(int(x)), end="\n\n")
