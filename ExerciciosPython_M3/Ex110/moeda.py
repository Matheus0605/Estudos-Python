def aumentar(preco=0, taxa=0, formatado=False):

    resp = preco + (preco * taxa/100)
    return resp if formatado is False else moeda(resp)

def diminuir(preco=0, taxa=0, formatado=False):

    resp = preco - (preco * taxa/100)
    return resp if formatado is False else moeda(resp)

def dobro(preco=0, formatado=False):

    resp = preco * 2
    return resp if formatado is False else moeda(resp)

def metade(preco=0, formatado=False):

    resp = preco / 2
    return resp if formatado is False else moeda(resp)

def moeda(preco=0, moeda='R$', formatado=False):

    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco=0, taxa=10, dim=5):

    print('_'*25)
    print('RESUMO DO VALOR'.center(25))
    print('_'*25)

    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{dim}% de redução: \t{diminuir(preco, dim, True)}')
    return preco , taxa, dim
