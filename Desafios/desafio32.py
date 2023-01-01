from calendar import isleap

ano = int(input('Digite um ano: '))
if isleap(ano):
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')