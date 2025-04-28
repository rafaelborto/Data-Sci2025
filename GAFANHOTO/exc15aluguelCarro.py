""" Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

kmRodados = float(input("Digite a quantidade de Km percorridos: "))
diasAlugados = int(input("Digite a quantidade de dias alugados: "))
preco = (60 * diasAlugados) + (0.15 * kmRodados)
print(f'O preço a pagar é de R$ {preco:.2f}!')
# O carro custa R$60 por dia e R$0,15 por Km rodado.