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