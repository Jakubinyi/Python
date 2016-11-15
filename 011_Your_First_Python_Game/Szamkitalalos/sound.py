import pygame

import time

pygame.init()

pygame.mixer.music.load(
    "~/Codecool/Python/011_Your_First_Python_Game/Szamkitalalos/ukulele.mp3")

pygame.mixer.music.play()

time.sleep(10)
