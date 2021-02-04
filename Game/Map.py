from PGinit import *
import pygame
from Player import *
from Obstacles import *


class Map:
    def __init__(self, player_: Player, obstacles_: Obstacles, scaleFactor=1):
        self.scaleFactor = scaleFactor
        self.player = player_
        self.obstacles = obstacles_

        self.player.link_obstacles(self.obstacles)
        self.player.scale(scaleFactor)
        self.obstacles.scale(scaleFactor)
        self.player.vision()

    def show(self):
        self.obstacles.show()
        self.player.vision()
        self.player.show()
        self.player.movements()




