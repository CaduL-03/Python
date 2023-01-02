i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
n = 0
result = i
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while n <= total:
        print('{}'.format(result), end='-> ')
        result = i + p
        i = result
        n += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print('FIM')