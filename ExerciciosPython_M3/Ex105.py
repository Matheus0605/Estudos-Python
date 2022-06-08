def notas(*num, sit=False):
    
    """
    -> Calcular nota e Situação do aluno.
    :param num: Possivel digitar quantas notas quiser.
    :param sit: (opcional) Mostra ou nao a Situação do alune.
    :return: O valor em dicionario da media e Situação do aluno.
    
    
    """
    lista_num = []
    for v in num:

        lista_num.append(v)

    lista_num.sort()
    print(lista_num)
    media = (lista_num[0] + lista_num[-1]) / 2
    fim = {'Total': len(lista_num), 'Maior': lista_num[-1], 'Menor': lista_num[0], 'Media': media}

    if sit:

        if media < 5:

            fim['Situação'] = 'RUIM'

        elif media > 5 and media < 7:

            fim['Situação'] = 'RAZOAVEL'

        else:

            fim['Situação'] = 'BOA'


    return fim

resp = notas(5.5, 6, 8, 10, sit=True)
print(resp)
help(notas)