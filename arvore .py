altura = input('disgite qual a altura da sua arvore número inteiteiro e positivo: ')
if altura .isnumeric():
    altura = int(altura)
    for i in range(altura):
        print(' '*(altura-i-1) + '*'*(2*i+1))
    print(' ' * ((altura * 2) // 5) + '|' * (altura))

else:
    print('o valor digitado nao é um número inteiro positivo')
