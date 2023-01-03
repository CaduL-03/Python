anos = 0
homens = 0
mulheres = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
            anos += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {anos}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
        
    


