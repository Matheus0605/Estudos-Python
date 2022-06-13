def leiaInt(msg):

    while True:

        try:

            num = int(input(msg))

        except (ValueError, TypeError):

            print('ERROR: Digite um numero valido!')
            continue

        except(KeyboardInterrupt):

            print('Usuario prefiriu nao digitar!')
            return 0

        else:

            return num

def leiaFloat(msg):

    while True:

        try:

            num = float(input(msg))

        except (ValueError, TypeError):

            print('ERROR: Digite um numero valido!')
            continue

        except(KeyboardInterrupt):

            print('Usuario prefiriu nao digitar!')
            return 0

        else:

            return num
            
n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um numero Real: ')
print(f'{n1} e {n2}')