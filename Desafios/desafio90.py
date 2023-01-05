alunos = {}
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
if alunos['Média'] < 5:
    alunos['Situação'] = 'Reprovado'
else:
    alunos['Situação'] = 'Aprovado'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
    

"""
pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': 19}
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f"{k} = {v}")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) 
del pessoas['sexo']

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # copy tem o mesmo propósito de [:] só que para dicionarios
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
"""