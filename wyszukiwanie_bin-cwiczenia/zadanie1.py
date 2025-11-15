"""
Zadanie 1: Najmniejsza wartość spełniająca warunek

Dana jest funkcja:

f(x) = 3x² + 7x + 2.

Dla danego k znajdź najmniejsze x ≥ 0, takie, że f(x) ≥ k.

Wejście: jedna liczba całkowita k ≤ 10^12
Wyjście: minimalne x.

Przykład: dla k=100; oczekiwany output to 5
"""


def f(x):
    return 3 * x ** 2 + 7 * x + 2


def znajdz_min_x(k):
    if k <= f(0):
        return 0

    lewy = 0
    prawy = 1
    while f(prawy) < k:
        prawy = prawy * 2

    while lewy < prawy:
        srodek = (lewy + prawy) // 2
        if f(srodek) >= k:
            prawy = srodek
        else:
            lewy = srodek + 1
    return lewy


print("naciśnij enter żeby zakończyć program")
while True:
    k = input(f"k=")
    if k == "":
        break
    else:
        print(znajdz_min_x(int(k)), end="\n\n")