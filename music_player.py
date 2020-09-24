import pygame


pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

while True:
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('panda.wav')
        pygame.mixer.music.play()
