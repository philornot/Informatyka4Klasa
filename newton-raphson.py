def oszacuj_pierwiastek(pierwiastek_do_kwadratu, dokladnosc=0.00001):
    pole_kwadratu = pierwiastek_do_kwadratu
    a = 1
    b = pole_kwadratu
    while abs(a - b) >= dokladnosc:
        a = (a + b) / 2
        b = pole_kwadratu / a
        # print(a, b)

    return (a + b) / 2


for i in range(15):
    oszacowany_pierw = oszacuj_pierwiastek(i + 1)
    print(f'Pierwiastek z {i + 1}: {oszacowany_pierw}')
