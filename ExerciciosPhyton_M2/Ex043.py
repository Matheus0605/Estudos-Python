'''– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual o peso atual (Kg): '))
altura = float(input('Qual sua altura (m): '))
imc = peso / (altura * altura)

print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Seu IMC está Abaixo do Peso')

elif imc >= 19 and imc <= 25:
    print('Seu IMC está no Peso Ideal!')

elif imc >= 26 and imc <= 30:
    print('Seu IMC está em Sobrepeso!')

elif imc >= 31 and imc <= 40:
    print('Seu IMC está Obesidade!')

else:
    print('Seu IMC está em Obesidade Morbida!')