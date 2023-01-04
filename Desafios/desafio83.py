expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(': # quando o input for ( ele joga na lista
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: # caso tenha ( na lista ele tira pra completar o par
            pilha.pop()
        else:
            pilha.append(')') # caso esteja vazio e não tiver seu par, ele coloca um ) na lista, fazendo o inválido
            break
if len(pilha) == 0: # se estiver vazio quer dizer que todo '(' teve seu ')' par
    print('Sua expressão está válida!!!')
else:
    print('Sua expressão está errada!!!')