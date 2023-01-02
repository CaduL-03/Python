r = 0
p = 0
for n in range(0, 7):
    nomes = int(input('Digite o seu ano de nascimento: '))
    if nomes <= 2005:
        n = r+1
    else:
        j = p+1
print('{} pessoa(s) são maiores de idade'.format(n))
print('{} pessoa(s) ainda não atingiram a maioridade'.format(j))