# Zadanie ze strony 4 z dokumentu: https://zpe.gov.pl/pdf/Ph4UJjypF

def algorytm_z_pseudokodu(x):
    x = x.split()
    n = len(x)
    # print(f'x={x}, n={n}')
    licznik = 0

    for i in range(n):
        # i jest cyfrą
        if "0" <= x[i] <= "9":
            licznik = licznik + 1

        # i jest operatorem
        if x[i] in ['+', '-', '*']:
            if licznik < 2:
                return licznik, "Nie"
            else:
                licznik = licznik - 1

    if licznik != 1:
        return licznik, "Nie"
    else:
        return licznik, "Tak"


napisy = [
    "1 2 + *",
    "1 2 + 3 4 - 5 * 7 8 + 9",
    "1 2 3 4 5 + + + +",
    "1 2 3 4 5 + + + + + +",
    "1 2 3 4 5 + + + + +",
    "1 2 + 2 3 - 3 4 * 4 5 + - - - -",
    "1 2 + 2 3 - 3 4 * 4 5 + - - - - -",
    "1 2 + 3 4 - 5 * 7 8 + 9 + + +"
]

for napis in napisy:
    wartosc_licznika, czy_poprawne = algorytm_z_pseudokodu(napis)
    print(f'\nNapis: "{napis}"'
          f'\nWartosć zmiennej licznik po zakończeniu algorytmu: {wartosc_licznika}\n'
          f'Czy wyrażnie jest poprawne w ONP: {czy_poprawne.upper()}')
