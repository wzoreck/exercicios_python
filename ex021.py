# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
import pygame
# pygame é para jogos mas podemos usar para reproduzir audios já que jogo tem audio
pygame.init() # primeiro precisa iniciar o pygame
pygame.mixer.music.load('star_wars.mp3')
pygame.mixer.music.play() # tocar a musica
pygame.event.wait()# esperar a musica acabar para terminar o programa
