lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
lado4 = int(input())

def eRetangulo(l1,l2,l3,l4):
    if (l1 == l2 and l3 == l4) or (l1 == l3 and l2 == l4) or (l1 == l4 and l2 == l3):
        return 'RETANGULO'
    else:
        return 'NAO EH UM RETANGULO'

print(eRetangulo(lado1,lado2,lado3,lado4))