sexo = str(input('Informe o sexo: ')).strip().upper()
while sexo != 'F' and sexo != 'M' :
    sexo = str(input('Digite um sexo valido: ')).strip().upper()
print(f'Sexo {sexo} ACEITO!')