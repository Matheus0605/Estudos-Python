print('='*25)
print('Banco Saque Leve'.center(25))
print('='*25)
valor_saque = int(input('Valor do saque: '))
soma = 0
nota_cinq = 0
nota_vin = 0
nota_dez = 0
nota_um = 0
while True:
    
    if valor_saque >= 50 :

        nota_cinq += 1
        valor_saque -= 50
    
    elif valor_saque < 50 and valor_saque > 20:

        nota_vin += 1
        valor_saque -= 20
    
    elif valor_saque < 20 and valor_saque > 10:

        nota_dez += 1
        valor_saque -= 10
        
    elif valor_saque < 10 and valor_saque > 0:

        nota_um += 1
        valor_saque -= 1
        
    elif valor_saque == 0:
        
        break

if nota_cinq > 0:

    print(f'Total de {nota_cinq} nota(s) de R$50') 

if nota_vin > 0:

    print(f'Total de {nota_vin} nota(s) de R$20') 

if nota_dez > 0:

    print(f'Total de {nota_dez} nota(s) de R$10')

if nota_um > 0:

    print(f'Total de {nota_um} nota(s) de R$1')
print('VOLTE SEMPRE!')