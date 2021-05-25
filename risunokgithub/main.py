import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1280, 680))
surf = pygame.Surface((220, 235), flags=pygame.SRCALPHA)
surf_palma = pygame.Surface((230, 350), flags=pygame.SRCALPHA)

rect(screen, (255, 175, 128), (0, 0, 1280, 680))


def bambuk(x, y, z):
    p = z
    line(surf_palma, (0, 104, 55), (114 + x, 263 + y + y * z), (114 + x, 340 + y + y * z), width=20)
    line(surf_palma, (0, 104, 55), (114 + x, 160 + y), (114 + x, 249 + y), width=20)
    line(surf_palma, (0, 104, 55), (121 + x, 98 + y), (112 + x, 149 + y), width=10)
    line(surf_palma, (0, 104, 55), (131 + x, 16 + y), (119 + x, 85 + y), width=8)
    screen.blit(surf_palma, (331 + x, 135 + y))

    # vetki
    def vetki(q, v, p):
        pi = 3.14
        arc(surf, (0, 104, 55), (130, 120, 90, 90), 0, 2 * pi / 3, width=1 * z)
        ellipse(surf, (0, 104, 55), (160, 120, 10, 50))
        ellipse(surf, (0, 104, 55), (175, 120, 10, 50))
        ellipse(surf, (0, 104, 55), (190, 125, 10, 50))

        arc(surf, (0, 104, 55), (30, 5, 190, 150), 0, pi / 2, width=1 * z)
        ellipse(surf, (0, 104, 55), (130, 5, 10, 50))
        ellipse(surf, (0, 104, 55), (145, 5, 10, 50))
        ellipse(surf, (0, 104, 55), (160, 10, 10, 50))
        ellipse(surf, (0, 104, 55), (175, 17, 10, 50))
        ellipse(surf, (0, 104, 55), (190, 25, 10, 50))
        if p == 0:
            screen.blit(surf, (q, v))
        if p == 1:
            flip = pygame.transform.flip(surf, True, False)
            screen.blit(flip, (q, v))

    vetki(208 + x, 183 + y, 0)
    vetki(468 + x, 173 + y, 1)


def panda(x, y, z):
    telo = pygame.Surface((300, 200), flags=pygame.SRCALPHA)
    ellipse(telo, (255, 255, 255), [0, 0, 300, 130])  # 800 420
    ellipse(telo, (0, 0, 0), (200, 60, 70, 100))

    znog = pygame.Surface((200, 200), flags=pygame.SRCALPHA)
    ellipse(znog, (0, 0, 0), (150, 40, 70, 110))
    rotz = pygame.transform.rotate(znog, 120)

    xnog = pygame.Surface((200, 200), flags=pygame.SRCALPHA)
    ellipse(xnog, (0, 0, 0), (60, 90, 40, 110))
    rotx = pygame.transform.rotate(xnog, 160)
    size = pygame.transform.scale(rotx, (200, 200))

    lico = pygame.Surface((200, 200), flags=pygame.SRCALPHA)
    ellipse(lico, (255, 255, 255), (30, 20, 120, 160))
    ellipse(lico, (0, 0, 0), (50, 130, 30, 30))
    ellipse(lico, (0, 0, 0), (40, 60, 30, 40))
    ellipse(lico, (0, 0, 0), (80, 60, 30, 40))
    ellipse(lico, (0, 0, 0), (40, 10, 30, 40))
    ellipse(lico, (0, 0, 0), (80, 10, 30, 40))

    lep = pygame.Surface((600, 600), flags=pygame.SRCALPHA)
    lep.blit(telo, (200, 260))
    lep.blit(rotz, (160, 300))
    lep.blit(rotx, (20, 260))
    lep.blit(lico, (130, 150))
    size = pygame.transform.scale(lep, (int(600*z), int(600*z)))
    screen.blit(size, (x-180, y-260))


panda(800, 420, 1)
panda(400, 420, 0.5)
bambuk(0, 0, 1)
bambuk(150, -100, 3)
bambuk(-150, -100, 3)
bambuk(570, -80, 3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
