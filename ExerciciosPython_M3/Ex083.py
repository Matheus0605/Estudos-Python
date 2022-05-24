expressao = input('Digite uma expressão: ')
cont = []

for simb in expressao:

    if simb == '(':

        cont.append('(')

    elif simb == ')':

        if len(cont) > 0:
            
            cont.pop()

        else:
            cont.append(')')
            break

if len(cont) == 0:

    print('Expressão válida')

else:

    print('Expressão inválida')
