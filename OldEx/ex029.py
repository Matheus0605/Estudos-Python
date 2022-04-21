#Confição Simples
vl = int(input('Qual é a velocidade atual do carro? '))
if vl > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h')
    n = (vl - 80) * 7
    print('Voce deve pagar uma multa de {:.2f}'.format(n))
print('Tenha um bom dia! Dirija com segurança!')