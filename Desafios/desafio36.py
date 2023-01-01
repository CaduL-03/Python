val = float(input('Qual o valor da casa ? '))
sal = float(input('Qual o seu salário mensal ? '))
anos = float(input('Em quantos anos irá pagar ?'))

mes = anos*12
porc = sal*0.3
par = val/mes

if porc > par:
    print('Seu financiamento foi aceito com parcelas no valor de ${:.1f} reais dividido em {} vezes'.format(par,mes))
else:
    print('Infelizmente você não pode financiar essa casa')


""" 
nome = str(input('Qual é seu nome ? '))
if nome == 'Carlos':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino. ')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}.'.format(nome))
 """
