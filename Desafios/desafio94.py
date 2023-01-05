pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa.clear()
    while True:
        pessoa['nome'] = str(input('Nome: '))
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'O grupo tem {len(galera)} pessoas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO!')