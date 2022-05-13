from mailbox import MaildirMessage


print('Gerando 10 termos de PA')
print('-='*15)
firstT = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = firstT
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='') 
        termo += razao
        cont += 1 
    print('PAUSA...')   
    mais = int(input('Quantos termos a mais você quer mostrar? ')) 
print(f'Ao todo tem {total} termos mostrados!')
