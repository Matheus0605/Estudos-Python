'''– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
from datetime import datetime

yearNow = datetime.today().year
yearBirth = int(input('Ano de nascimento: '))
age = yearNow - yearBirth

if age <= 9:
    print(f'O atleta tem {age}')
    print('Classificação: MIRIN')

elif age == 10 or age <= 14:
    print(f'O atleta tem {age} anos') 
    print('Classificação: INFANTIL')

elif age == 15 or age <= 19:
    print(f'O atleta tem {age} anos') 
    print('Classificação: JUNIOR')

elif age == 20 or age <=25:
    print(f'O atleta tem {age} anos') 
    print('Classificação: SÊNIOR')

elif age > 25:
    print(f'O atleta tem {age} anos') 
    print('Classificação: MASTER')