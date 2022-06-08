PAHT = "Desafio Toni/aluguel.txt"

with open(PAHT, "r", encoding="utf-8") as arquivo:

    cadastros = {}
    usuarios = []
    lista = []
    
    for linha in arquivo.readlines():

        nome = linha.split()
        lista.append(nome)

    """Experiencia do Usuário com Login """

    while True:

        acesso = int(input("[1] Entrar\n[2] Cadastrar\n."))

        if acesso == 1:

            print('Programa novo! 0 cadastro existentes')
            break

        elif acesso == 2:    
            
            cadastros['Login'] = str(input('Login: '))
            cadastros['Password'] = int(input('Senha:[4 NUMEROS] '))
            cadastros['Nome'] = str(input('Nome de Exibição: '))
            break

        else: 

            print('ERRO! Me sinalize um valor existente!')

print('-='*30)        
print(cadastros)
print(lista)