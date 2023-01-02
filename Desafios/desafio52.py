num = int(input('Digite um número: '))
primos = []
for c in range(1, num+1):
    if num % c ==0:
        primos.append(c)
    if len(primos) == 2:
        print('O número é primo')
    else:
        print('O número não é primo')