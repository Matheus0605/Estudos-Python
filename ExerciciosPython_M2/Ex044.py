'''– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

from xml.dom.expatbuilder import parseFragment


value = float(input('Valor da compra: '))
print('-'*12 +' Opções de pagamento ' + '-'*12)
print('[1] À vista dinheiro (10% de desconto)\n[2] À vista no cartão (5% de desconto)\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
escolha = int(input('Escolha: '))

if escolha == 1:
    pagament = value - value * 10 / 100
    print('Sua compra de R${:.2f} terá o valor final de R${:.2f} '.format(value,pagament))

elif escolha == 2:
    pagament = value - value * 5 / 100
    print('Sua compra de R${:.2f} terá o valor final de R${:.2f}'.format(value,pagament))

elif escolha == 3:
    pagament = value / 2
    print('Sua compra de R${:.2f} terá parcelas de R${:.2f} em 2x'.format(value,pagament))

elif escolha == 4:
    parcela = int(input('Quantas parcelas: '))
    pagament = (value + value * 20 / 100) / parcela
    print('Sua compra de R${:.2f} terá parcelas de R${:.2f} em 3x'.format(value,pagament))