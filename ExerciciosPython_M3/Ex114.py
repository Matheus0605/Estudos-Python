from urllib import request
from urllib.error import URLError 

site = str(input('insira o site: '))

try:

    url=request.urlopen('https://www.'+site+'.com/')

except URLError:
    
    print('Erro ao entrar no site')

else:

    print('O site foi aberto com sucesso')
