num1 = int(input('Digite um número'))
print('''Escolha uma das bases para a conversão:
        [1] Converter para binário
        [2] Converter para octal
        [3] Conveter para hexadecimal''')#as 3 aspas servem para quebrar a linha
opcao = int(input('Sua opção'))
if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(num1,bin(num1)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num1,oct(num1)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num1,hex(num1)))
else:
    print('Opção inválida, tente novamente.')
