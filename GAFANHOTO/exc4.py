var1 = input('Digite algo: ')
print("O tipo primitivo desse valor é", type(var1))
print('Só tem espaço:', var1.isspace()) #RETORNA SE HÁ APENAS ESPAÇOS
print('É um número?', var1.isnumeric())
print('É alfabético?', var1.isalpha())
print('É alfanumérico?', var1.isalnum())
print('Está tudo em maiúsculas?', var1.isupper())
print('Está tudo em minúsculas?', var1.islower())
print(f'APENAS a primeira letra maiúscula? {var1.istitle()}.') #RETORNA TRUE APENAS SE A PRIMEIRA LETRA FOR MAIÚSCULA
