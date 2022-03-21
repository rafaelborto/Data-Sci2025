import forca
import jogo_da_adivinhacao_pt6_niveis_e_pontos

print(40 * "*")
print("Escolha o jogo que você quer:")
print(40 * "*")

print("(1) Forca (2) Adivinhação")

jogo = int(input('Qual jogo?'))

if jogo == 1:
    print('Jogando Forca')
else:
    print('Jogando Adivinhação')