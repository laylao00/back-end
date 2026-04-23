from math import cos,sin,tan,radians
ang = float(input('Digite o valor do seu ângulo'))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} tem seno de {:.2f}'.format(ang,seno))
print('O ângulo de {} tem cosseno de {:.2f}'.format(ang,coss))
print('O ângulo de {} tem tangente de {:.2f}'.format(ang,tang))
