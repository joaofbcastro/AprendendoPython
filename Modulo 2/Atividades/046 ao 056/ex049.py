# Tábuada
n = int(input('\nVocê quer ver a tábuada do: '))
for c in range(1, 11):
    print('{} * {:2} = {}'.format(n, c, n*c))
print('')
