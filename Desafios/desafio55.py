maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso capturado foi {} e o menor peso {}'.format(maior,menor))