preço = float(input('Qual o preço do produto ? '))
print(""" Escolha a forma de pagamento:
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
 """)
opção = int(input('Sua opção: '))

dich = preço - (preço*0.1)  
visca = preço - (preço*0.05)
cadiv = (preço*0.2) + preço

if opção == 1:
    print('${} reais o preço a pagar.'.format(dich))
elif opção == 2:
    print('${} reais o preço a pagar.'.format(visca))
elif opção == 3:
    print('${} reais o preço a pagar.'.format(preço))
elif opção == 4:
    print('${} reais o preço a pagar.'.format(cadiv))
else:
    print('Opção inválida, tente novamente')