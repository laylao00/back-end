while True:
    num = int(input('Quer ver a tabuada de valor?'))
    if num<0:
        break
    print('-'*20)
    for c in range(1,11):
        print(f'{num} x {c:2d} = {num * c}')
    print('-'*20)
print('''PROGRAMA TABUADA: ENCERRADO
      Volte sempre!''')
