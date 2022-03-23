import forca
import jogo_da_adivinhacao_pt6_niveis_e_pontos

def jogar():
    print(40 * "*")
    print("Escolha o jogo que você quer:")
    print(40 * "*")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input('Qual jogo?'))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()

    else:
        print('Jogando Adivinhação')
        jogo_da_adivinhacao_pt6_niveis_e_pontos.jogar()

if __name__ = 'main':
    jogar()