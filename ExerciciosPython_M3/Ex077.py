tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO' )

for c in tupla:

    print(f'\nNa palavra {c} temos ', end='')

    for letra in c:    

        if letra.lower() in 'aeiou':

            print(letra, end=' ')
            