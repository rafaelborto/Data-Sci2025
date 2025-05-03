# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input("Digite um número de 0 a 9999: "))

numero = str(numero).zfill(4)  # Preenche com zeros à esquerda, se necessário

print(
     f'Unidade: {numero[-1]}'
     f'\nDezena: {numero[-2]}'
     f'\nCentena: {numero[-3]}' 
     f'\nMilhar: {numero[-4]}')



Ou poderia fazer assim, utlizando o operador de divisão e o resto da divisão:
# numero = int(input("Digite um número de 0 a 9999: "))
# unidade = numero % 10
# dezena = (numero // 10) % 10
# centena = (numero // 100) % 10
# milhar = (numero // 1000) % 10