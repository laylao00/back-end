x = float(input('Digite a largura'))
y = float(input('Digite a altura'))
A = x*y
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m quadrados;'.format(x,y,A))
print('Para pintar essa parede, você precisa de {}L de tinta'.format(A/2))
