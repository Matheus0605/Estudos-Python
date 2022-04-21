larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual altura da parede? '))
area = larg * alt
print('A área da sua parede é de {:.3f}m'.format(area))
print('Para pinta essa parede, você precisará de {:.4f}L de tinta'.format(area/2))