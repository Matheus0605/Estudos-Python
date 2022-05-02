salary = float(input('Qual o salário do funcionario? R$ '))

if salary <= 1250:
    newSalary = salary + (salary * 15 / 100)
else:
    newSalary = salary + (salary * 10 / 100)
    
print('Quem ganhava {:.2f} agora passar a ganhar {:.2f}'.format(salary, newSalary))