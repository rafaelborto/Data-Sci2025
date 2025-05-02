# 20. Crie um programa que sorteie uma lista de nomes fornecida pelo usuário e exiba a lista em ordem aleatória.

# # O programa deve solicitar ao usuário que insira uma lista de nomes separados por vírgula e, em seguida, exibir a lista em uma ordem aleatória.  

# # Exemplo de entrada: "Ana, João, Maria, Pedro"

import random  # Importa a função shuffle do módulo random para embaralhar a lista
# shuffle() embaralha a lista de forma aleatória, alterando a ordem dos elementos na lista original.

lista1 = ["Ana", "João", "Maria", "Pedro"]


# O método .split(",") divide a string em uma lista de nomes, usando a vírgula como delimitador. [OU SEJA, A VÍRGULA NÃO É INCLUÍDA NA LISTA]

print("Lista original:", lista1)

# original = lista1.copy()  # Faz uma cópia da lista original para preservar a ordem original

print('A ordem de apresentação será: ', random.shuffle(lista1), "Retorna NONE "
      "porque eu não atribuí o embaralhamento antes de chamar a lista.")  # Exibe a lista embaralhada



""" 🔄 Por que random.shuffle() retorna None?
O método random.shuffle() é projetado para alterar a ordem dos elementos da lista fornecida diretamente, sem criar uma nova lista. Essa abordagem é eficiente em termos de memória e segue a filosofia do Python de que "explícito é melhor que implícito". Como resultado, ele não retorna a lista modificada, mas sim None.

Para que o código funcione conforme o esperado, você deve chamar random.shuffle(lista1) em uma linha separada e, em seguida, imprimir lista1. Veja o exemplo corrigido: """

random.shuffle(lista1)  # Embaralha a lista original de forma aleatória
print('A ordem de apresentação será: ', lista1)  # Exibe a lista embaralhada
