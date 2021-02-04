import requests
from bs4 import BeautifulSoup
import re
import time
import pygame
import math
import random
from colour import Color
import numpy
from multiprocessing import Process
import Player
import Obstacle
import Obstacles
from ObstacleRectangle import *
import Map
import GameScreen
from Funcs import *


if __name__ == '__main__':
    running = True
    # СОЗДАНИЕ ОБЪЕКТОВ
    pygame.mouse.set_visible(False)
    player = Player.Player([300, 300])
    obstacles = Obstacles.Obstacles()
    obstacles.add_obstacle(ObstacleRectangle([screenWidth / 2, screenHeight / 2],
                                             screenWidth, screenHeight, BLACK, WHITE))
    obstacles.add_obstacle(ObstacleRectangle([400, 425], 100, 100))
    obstacles.add_obstacle(ObstacleRectangle([400, 225], 100, 100))
    mapp = Map.Map(player, obstacles, 0.25)
    gameScreen = GameScreen.GameScreen(mapp)

    # ОКОНЧАНИЕ ГСОЗДАНИЕ ОБЪЕКТОВ
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.event.pump()
        pygame.time.delay(16)

        screen.fill((222, 184, 135))
        pygame.draw.rect(screen, (64, 224, 208),
                            [0, 0, screenWidth, screenHeight / 2 - gameScreen.curYShift])


        gameScreen.show()
        mapp.show()



        pygame.display.update()


    pygame.quit()
















