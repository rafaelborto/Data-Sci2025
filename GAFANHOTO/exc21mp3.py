"para instalar o pygame, USE NO TERMINAL: PIP INSTALL PYGAME"

import pygame  # Importa o módulo pygame para criar jogos e multimídia

pygame.init()  # Inicializa todos os módulos do pygame
pygame.mixer.music.load("exc21.mp3")  # Carrega o arquivo de música "musica.mp3"
pygame.mixer.music.play()  # Inicia a reprodução da música
pygame.event.wait()  # Aguarda até que um evento ocorra (como o término da música)



""" pygame.mixer.music.set_volume(0.5)  # Define o volume da música (0.0 a 1.0)
pygame.mixer.music.pause()  # Pausa a música
pygame.mixer.music.unpause()  # Retoma a reprodução da música
pygame.mixer.music.stop()  # Para a reprodução da música
pygame.mixer.music.fadeout(1000)  # Faz a música diminuir gradualmente em 1 segundo (1000 milissegundos)
pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Define um evento personalizado quando a música termina """