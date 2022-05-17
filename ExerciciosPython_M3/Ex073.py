tabela  = ('Corinthians', 'Santos', 'Avai', 'América-MG', 'Bragantino', 'Atletico-MG', 'São Paulo', 'Botafogo', 'Internacional', 'Coritiba', 
'Cuiabá', 'Atletico-PR', 'Palmeiras', 'Flamengo', 'Fluminense', 'Goiás', 'Ceará SC', 'Juventude', 'Atlético-GO', 'Fortaleza')

print(f'Lista do Brasileirao 2022: {tabela}')
print('-='*50)
print(f'Os 5 primeiro são: {tabela[0:5]}')
print('-='*50)
print(f'Os 4 ultimos são: {tabela[16:20]}')
print('-='*50)
print(f'Os times em ordem Alfabetica fica: {sorted(tabela)}')
print('-='*50)
if  'Chapecoense' not in tabela :
    print('Chapecoense nao esta na Tabela')