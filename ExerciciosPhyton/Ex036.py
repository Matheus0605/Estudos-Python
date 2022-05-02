value = float(input('Valor da casa: '))
salary = float(input('Salario do comprador: '))
time = int(input('Quantos anos de financiamento: '))
prestacao = value / (12 * time)

print('Para pagar uma casa de {:.2f} em {} anos prestação será de R${:.2f}'.format(value,time,prestacao))
if prestacao > salary * 30 / 100:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO!')
