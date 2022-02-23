# Faça um programa em Python que abra e reproduza o aúdio de um
# arquivo MP3
'''
import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()
# Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
'''


import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ARQUIVO ESCOLHIDO')
pygame.mixer.music.play()
input()
pygame.event.wait()