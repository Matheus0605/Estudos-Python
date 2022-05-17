import math
catOp = float(input('Comprimento do cateto Oposto: ')) 
catAd = float(input('Comprimento do cateto Adjacente: '))
hi = math.hypot(catOp,catAd)
print('A hipotenusa vai medir {:.2f}'.format(hi))

