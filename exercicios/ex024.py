cidade = str(input('Em que cidade você nasceu? ')).strip()
comeca_com_santo = cidade[:5].lower() == 'santo'
if comeca_com_santo == True:
    print('Sim, o nome da sua cidade começa com "santo"!')
else:
    print('Não, o nome da sua cidade não começa com "santo".')


_________________________________________


cidade = str(input('Em que cidade vocẽ nasceu?'))
n1 = cidade.lower()
print('santo' in n1)
