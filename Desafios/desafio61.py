i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
n = 0
result = i
while n <= 9:
    print('{}'.format(result), end='-> ')
    result = i + p
    i = result
    n += 1
print('Acabou')