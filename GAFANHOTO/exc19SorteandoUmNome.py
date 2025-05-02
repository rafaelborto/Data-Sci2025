from random import choice
# 19. Crie um programa que sorteie um nome de uma lista de nomes fornecida pelo usuário.
# O programa deve solicitar ao usuário que insira uma lista de nomes separados por vírgula e, em seguida, escolher aleatoriamente um nome dessa lista.
# O nome sorteado deve ser exibido na tela.
# Exemplo de entrada: "Ana, João, Maria, Pedro"


lista1 = input("Digite uma lista de nomes separados por vírgula: ").split(",") 

# O método .split(",") divide a string em uma lista de nomes, usando a vírgula como delimitador. [OU SEJA, A VÍRGULA NÃO É INCLUÍDA NA LISTA]

# O resultado é uma lista de nomes, onde cada nome é um elemento da lista.  

print("Lista original:", lista1)

print("Nome sorteado:", choice(lista1).strip())

# o método .strip é utilizado para remover espaços em branco no início e no final de cada nome, garantindo que não haja espaços indesejados ao redor dos nomes.

