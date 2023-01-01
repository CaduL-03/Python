r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r2+r3 < r1 or r3+r1 < r2 or r1+r2 < r3:
    print('As retas não formam um triângulo!') 
else:
    print('Formam um triângulo!')

if r1 == r2 and r1 == r3:
    print('É um triângulo equilátero.')
elif r1 != r2 
    print('É um triângulo isósceles.')