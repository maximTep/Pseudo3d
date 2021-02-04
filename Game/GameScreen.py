from PGinit import *
import pygame
import Obstacles
import ObstacleRectangle
import Obstacle
from Funcs import *
from Map import *
import math
import numpy


class GameScreen:
    def __init__(self, map_: Map):
        self.map = map_
        self.mx = pygame.mouse.get_pos()[0]
        self.my = pygame.mouse.get_pos()[1]
        self.curYShift = 0
        self.maxYShift = 500
        #self.map.player.visionFrequency = 0.05


    def wall_height(self, distance):
        return (screenHeight / self.map.scaleFactor) / (distance * math.cos(self.map.player.visionAngle / 2))

    def show(self):
        visionPoints = self.map.player.visionPoints
        if screenWidth % len(visionPoints) != 0:
            segment_width = segment_width = screenWidth // len(visionPoints) + 1
        else:
            segment_width = segment_width = screenWidth // len(visionPoints)

        screen_parts = [[0, segment_width]]
        for i in range(len(visionPoints)-1):
            screen_parts.append([screen_parts[-1][1], screen_parts[-1][1] + segment_width])

        new_pos = pygame.mouse.get_pos()
        x_diff = new_pos[0] - self.mx
        y_diff = new_pos[1] - self.my
        self.mx, self.my = pygame.mouse.get_pos()
        if self.curYShift + y_diff > self.maxYShift:
            self.curYShift = self.maxYShift
        else:
            self.curYShift += y_diff * 3
        for ind, part in enumerate(reversed(screen_parts)):
            if self.map.player.is_collided(ind):
                distance = dist(self.map.player.pos, visionPoints[ind])
                player_angle = self.map.player.angle
                player_line = [self.map.player.pos,
                               [self.map.player.pos[0] + math.cos(player_angle),
                                self.map.player.pos[1] - math.sin(player_angle)]]
                cosa = math.cos(get_angle([self.map.player.pos, visionPoints[ind]], player_line))
                wall_h = (screenHeight / self.map.scaleFactor) / (distance * cosa)
                max_dist = self.map.player.visionRadius
                color = (120 - 120 * (distance / max_dist) ** (1/3),
                         120 - 120 * (distance / max_dist) ** (1/3),
                         120 - 120 * (distance / max_dist) ** (1/3))
                pygame.draw.rect(screen, color,
                                 [part[0], (screenHeight - wall_h) / 2 - self.curYShift,
                                  part[1] - part[0],
                                  wall_h])

                # rect1 = pygame.Rect((part[0], (screenHeight - wall_h) / 2 - self.curYShift,
                #                     part[1] - part[0],
                #                     wall_h))
                # wall_image = pygame.image.load('wall_texture.jpg')
                # screen.blit(wall_image,
                #             [part[0], (screenHeight - wall_h) / 2 - self.curYShift])




