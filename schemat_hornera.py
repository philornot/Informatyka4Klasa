wsp = [-5, 1, -2, 0, 3]  # dla W(x) = 3x^4 - 2x^2 + x - 5
st = len(wsp) - 1 # st(W(x)) = 4
m_zer = -2

wynik = [0] * (st + 1)
print(f'wynik: {wynik}')
print(f'wsp: {wsp}')

for i in range(st+1, 1, -1): # od indeksu ostatniego (len(wsp)) do 0
    if i == st+1:
        wynik[st-1] = wsp[st]
    else:
        print(i, wynik)
        wynik[i] = wynik[i+1] * m_zer + wsp[i] # poprzedni wynik * miejsce zerowe + obecny współczynnik

    if i == 0:
        wynik[i] = wynik[i+1] * m_zer + wsp[i]

print(wynik)