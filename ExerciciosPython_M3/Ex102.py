def fatorial(num, show=False):
    """
    -> Calculo Fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostra ou nao a conta.
    :return: O valor do Fatorial de um numero n.    
    """

    fa = 1
    for v in range(num, 0, -1):
        if show:

            print(v, end='')

            if v>1:

                print(' x ', end='')

            else:

                print(' = ', end='')
        fa *= v
    return fa


print(fatorial(5, True))
print(fatorial(10, True))
