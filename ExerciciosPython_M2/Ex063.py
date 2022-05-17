print('-'*20)
print('Sequancia de Fibonacci')
print('-'*20)

termos = int(input('Quantos termos você quer mostrar? '))
fn1 = 0
fn2 = 1
cont = 3

print('~'*20)
print(f'{fn1} -> {fn2}', end='')
while cont <= termos:
    fn = fn1 + fn2
    print(f' -> {fn}', end=' ')
    fn1 = fn2
    fn2 = fn
    cont += 1
print('FIM')
print('~'*20)

