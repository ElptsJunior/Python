print('''
Build an program in python that open and play an M.P.3 file 
''')

import pygame
# starting pygame
pygame.init()
# load MP3 file and playing
pygame.mixer.music.load('sendmeanangel.mp3')
pygame.mixer.music.play()
pygame.event.wait()

