print(40 * "*")
print("Bem vindo ao jogo da adivinhação")
print(40 * "*")
import random

num_secreto = round(random.randrange(1, 101))
chances = 0
rodada = 1
pontos = 1000

print('Qual nível de dificuldade você quer?'
      '\n(1) Fácil'
      '\n(2) Médio'
      '\n(3) Difícil')
nivel = int(input('Defina um nível: '))

if nivel == 1:
    chances = 10
elif nivel == 2:
    chances = 7
else:
    chances = 5

print("Você tem", chances, "chances para acertar!")

for rodada in range(1, chances + 1):

    print("Tentativa {} de {}".format(rodada, chances))
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("Você digitou", chute, end='.')

    if chute < 1 or chute > 100:
        print("\nEsse número não é válido")
        continue

    acertou = chute == num_secreto
    maior = chute > num_secreto
    menor = chute < num_secreto
    pontos_perdidos = abs(chute - num_secreto)
    pontos = pontos - pontos_perdidos

    if acertou:
        print("\nVocê acertou e fez {} pontos! :)".format(pontos))
        break
    elif maior:
        print("\nSeu chute foi maior do que o número. Você errou! :(")
        if (rodada == chances):
            print("O número secreto era {}. Você fez {}".format(num_secreto, pontos))
    elif menor:
        print("\nSeu chute foi menor do que o número. Você errou! :(")
        if (rodada == chances):
            print("O número secreto era {}. Você fez {}".format(num_secreto, pontos))

print("Fim de Jogo")
