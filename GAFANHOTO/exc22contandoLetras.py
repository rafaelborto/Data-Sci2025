
# Exercício Python 22: 
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas e minúsculas.
# 2. Quantas letras tem o primeiro nome e o nome completo (sem considerar espaços).


nomeCompleto = str(input('Digite seu nome completo: ')).strip() # remove espaços no início e no fim da string
print(f'1. Seu nome em maiúsculas é: {nomeCompleto.upper()}')
print(f'2. Seu nome em minúsculas é: {nomeCompleto.lower()}')

nomeLista = nomeCompleto.split(' ')
primeiroNome = nomeLista[0]

nomeSemEspacos = ''.join(nomeLista)
print(f'2. Seu nome sem espaços é: {nomeSemEspacos}')


print(f'3. Seu primeiro nome contém {len(primeiroNome)} letras.') 

# print('seu primeiro nome contém: {nomeCompleto.find(" ")} letras.') # ou seja, o número de letras do primeiro nome é o número de letras até o primeiro espaço, porque a contagem começa do 0. Ana = 0, 1 e 2, ou seja, 3 letras. o primeiro espaço é o 3.


print(f'4. Seu nome completo contém {len(nomeSemEspacos)} letras.')
#print(f'4. Seu nome completo contém {len(nomeCompleto) - nomeCompleto.count(" ")} letras.') # ou seja, o número de letras do nome completo é o número de letras menos o número de espaços.

# outra forma de fazer seria: nomeCompleto.replace(' '.'').len()



