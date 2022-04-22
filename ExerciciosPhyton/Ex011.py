larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual altura da parede? '))
area = larg * alt
print('A área da sua parede é de {}m'.format(area))
print('Para pinta essa parede, você precisará de {}L de tinta'.format(area/2))