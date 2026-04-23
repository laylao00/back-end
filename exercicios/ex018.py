from math import hypot
ca = float(input('Digite o cateto adjacente'))
co = float(input('Digite o cateto oposto'))
h = hypot(ca,co)
print('A hipotenusa vai medir {}'.format(h))

catad = float(input('Digite o cateto adjacente'))
catop = float(input('Digite o cateto oposto'))
hi = (catad**2 + catop**2)**0.5
print('O cateto adjacente é {}, o oposto é {} e a hipotenusa mede {}.'.format(catad,catop,hi))
