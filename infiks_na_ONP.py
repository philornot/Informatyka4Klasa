raw_input = input('Wprowadź działania (pamiętaj o spacjach):\n')

inpt = raw_input.split(' ')
stos = []


def zamien_infiks_na_onp(infiks):
    print(infiks, end='\n\n')
    for i in infiks:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print(f'{i} to liczba')

        elif i not in ['(', ')']:
            print(f'{i} to nawias')

        else:
            print(f'{i} to operator')


print(zamien_infiks_na_onp(inpt))
