velocity = float(input('Qual a velocidade do carro? '))

if velocity > 80:
    multa = (velocity - 80) * 7.0 
    print('MUTADO! Voce exceudeu o limite permitido de 80km')
    print('Você deve pagar uma multa no valor de R${:.2f}'.format(multa))
else:
    print('Ok! Ande com segurança!')