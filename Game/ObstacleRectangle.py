from PGinit import *
import pygame
from Obstacle import *


class ObstacleRectangle(Obstacle):
    def __init__(self,  pos: list, width: int, height: int, outColor=BLACK, fillColor=HZ):
        super().__init__()
        self.pos = pos
        self.width = width
        self.height = height
        self.outColor = outColor
        self.fillColor = fillColor
        self.set_edges()

    def scale(self, scaleFactor):
        self.pos = [self.pos[0] * scaleFactor, self.pos[1] * scaleFactor]
        self.width = self.width * scaleFactor
        self.height = self.height * scaleFactor
        self.set_edges()

    def set_edges(self):
        self.edges.clear()
        self.points.clear()
        start_point = [self.pos[0] - self.width / 2, self.pos[1] + self.height / 2]
        end_point = [start_point[0] + self.width, start_point[1]]
        self.edges.append([start_point, end_point])
        self.points.append(start_point)

        start_point = end_point
        end_point = [end_point[0], end_point[1] - self.height]
        self.edges.append([start_point, end_point])
        self.points.append(start_point)

        start_point = end_point
        end_point = [end_point[0] - self.width, end_point[1]]
        self.edges.append([start_point, end_point])
        self.points.append(start_point)

        start_point = end_point
        end_point = [end_point[0], end_point[1] + self.height]
        self.edges.append([start_point, end_point])
        self.points.append(start_point)






