valores = []

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Você digitou os valores {sorted(valores)}')