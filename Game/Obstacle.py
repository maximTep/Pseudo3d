from PGinit import *
import pygame



class Obstacle:
    def __init__(self):
        self.edges = []
        self.points = []
        self.outColor = BLACK
        self.fillColor = HZ

    def show(self):
        pygame.draw.polygon(screen, self.fillColor, self.points)
        pygame.draw.aalines(screen, self.outColor, True, self.points)

