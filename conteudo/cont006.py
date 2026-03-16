## OPERADORES
# Podemos escrever um resultado na quantidade de caracteres específicas 
# ao colocar o valor dentro da mascára após escrever
nome = input('Qual o seu nome?')
print('Prazer em conhece-lo {:20}!'.format(nome))

##ALINHAMENTO DE MASCÁRAS

# Podemos alinhar o nome dentro do número de caracteres que desejamos
# Alinhamento para a direita
nome = input('Qual é o seu nome?')
print('Prazer em conhece-lo {:>20}1'.format(nome))

# Alinhamento para a esquerda
nome = input('Qual é o seu nome?')
print('Prazer em conhece-lo {:<20}1'.format(nome))

# Alinhamento para o centro
nome = input('Qual é o seu nome?')
print('Prazer em conhece-lo {:^20}1'.format(nome))
