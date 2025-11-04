def oszacuj_pierwiastek(pierwiastek_do_kwadratu, dokladnosc=0.00001):
    pole_kwadratu = pierwiastek_do_kwadratu
    a = 1
    b = pole_kwadratu
    licznik = 0
    while abs(a - b) >= dokladnosc:
        a = (a + b) / 2
        b = pole_kwadratu / a
        licznik += 1

    wynik = (a + b) / 2
    return wynik, licznik


c = 35
oszacowany_pierw, wykonania = oszacuj_pierwiastek(c, dokladnosc=0.0001)
print(f'Pierwiastek z {c}: {oszacowany_pierw}, było {wykonania} wykonań funkcji.')
