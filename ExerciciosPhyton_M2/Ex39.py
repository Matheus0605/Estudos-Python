from datetime import datetime
yearNasc = int(input('Ano de nascimento: '))
yearNow = datetime.today().year
idade = yearNow - yearNasc


print(f'Quem nasceu no ano de {yearNasc} tem {idade} anos em {yearNow}')
if idade < 18:
    print('Ainda nao esta em tempo de se alistar')
    print(f'Faltam {18 - idade} anos para se alistar')
elif idade > 18:
    print('Passou de sua fase de alistamento')
    print(f'Se passaram {idade - 18} anos desde o alistamneto')
else:
    print('Voce ja tem 18 anos e tem idade para se alistar')
