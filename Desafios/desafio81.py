valores = []

while True:
    valores.append(int(input('Digite um valor: ')))

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-='*15)
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')