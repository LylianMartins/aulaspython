'''Faça um programa em Python que abra e reproduza o áudio de um arquivo em MP3'''



import pygame
pygame.mixer.init()
pygame.mixer.music.load('Sweet_Relief.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

pygame.quit()


'''import pygame
pygame.init()
pygame.mixer.music.load('Sweet_Relief.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

