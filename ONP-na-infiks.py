raw_input = input('Wprowadź działania (pamiętaj o spacjach):\n')

# a = '2 3 4 / +'
# b = '2 3 * 4 -'
# f = '1 3 5 7 * 2 + ^ 9 + -'
# j = '9 8 + 4 3 2 * + 7 6 + ^ 5 - *'

inpt = raw_input.split(' ')
stos = []


def zamien_onp_na_infiks(onp):
    print(onp, end='\n\n')
    for i in onp:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print(f'{i} to liczba')
            stos.append(i)
            print(f'Dodaję {i} do stosu: stos={stos}\n')
        else:
            print(f'{i} to znak')
            a = stos.pop(-1)
            b = stos.pop(-1)
            dzialanie = f'{b} {i} {a}'
            print(f'a={a}, b={b}, dzialanie={dzialanie}')
            stos.append(dzialanie)

    output = f'\nWYNIK:\n{dzialanie}'
    return output


print(zamien_onp_na_infiks(inpt))
