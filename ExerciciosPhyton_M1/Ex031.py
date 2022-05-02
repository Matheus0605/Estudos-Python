km = int(input("Qual a distancia da viagem em km's: "))

if km <= 200:
    value = km * 0.50
    print('Total a pagar pela viagem: R${:.2f}'.format(value))
else:
    value = km * 0.45
    print('Total a pagar pela viagem: R${:.2f}'.format(value))