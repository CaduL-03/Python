soma = 0
m1000 = 0
menor = 0
contador = 0
while True:
    print('-'*30)
    print('LOJA DESCONTÃO')
    print('-'*30)
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    contador += 1
    soma += p
    if p > 1000:
        m1000 += 1
    if contador == 1:
        menor = p
    else:
        if p < menor:
            menor = p
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('{:-^40}'.format('FIM DAS COMPRAS'))
print(f'O total da compra foi R${soma}')
print(f'Temos {m1000} produto(s) custando R$1000')
print(f'O produto mais barato custa R${menor}')