km = float(input("Quantos Km's foram percorridos? "))
dias = float(input('Por quantos dias foi alugado? '))
total = (60 * dias) + (0.15 * km)
print('Total a pagar: R${:.2f}'.format(total))
