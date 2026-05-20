nome = str(input('Qual é o seu nome?'))
if  nome == 'Laylon':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in "Ana Claúdia Jessica Juliana":
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia {}.'.format(nome))
