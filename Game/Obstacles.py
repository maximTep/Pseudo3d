from PGinit import *
import pygame
import Obstacle
from Funcs import *
import math


class Obstacles:
    def __init__(self):
        self.obstacles = []

    def scale(self, scaleFactor):
        for obstacle in self.obstacles:
            obstacle.scale(scaleFactor)

    def show(self):
        for obstacle in self.obstacles:
            obstacle.show()

    def add_obstacle(self, obstacle: Obstacle):
        self.obstacles.append(obstacle)





