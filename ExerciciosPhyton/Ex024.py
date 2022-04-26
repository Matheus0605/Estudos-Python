print('Cidade validas; todas que tem a palavra "Santo(s)".')
city = str(input('Em que cidade você nasceu? '))
verify =  city.upper().strip()
print('SANTO' in verify)