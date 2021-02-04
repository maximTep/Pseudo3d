from PGinit import *
import pygame
import Obstacles
import ObstacleRectangle
import Obstacle
from Funcs import *
import math
import numpy
import copy


class Player:
    def __init__(self, pos: list, obstacles_obj=None):
        self.pos = pos
        self.scaleFactor = 1
        self.size = 20
        self.angle = -45 * math.pi / 180
        self.moveSpeed = 3
        self.rotateSpeed = 0.5
        self.visionAngle = 90 * math.pi / 180
        self.visionRadius = 1500
        self.visionFrequency = 0.01
        self.collisionFrequency = 0.5
        self.collisionRadius = self.size + 2
        self.obstacles = obstacles_obj
        self.visionPoints = []
        self.collidedPoints = []
        self.mx = pygame.mouse.get_pos()[0]
        self.my = pygame.mouse.get_pos()[1]


    def scale(self, scaleFactor):
        self.scaleFactor = scaleFactor
        self.pos = [self.pos[0] * scaleFactor, self.pos[1] * scaleFactor]
        self.size = self.size * self.scaleFactor
        self.moveSpeed = self.moveSpeed * self.scaleFactor
        self.visionRadius = self.visionRadius * self.scaleFactor
        self.collisionRadius = (self.size + 2) * self.scaleFactor


    def link_obstacles(self, obstacles_obj: Obstacles):
        self.obstacles = obstacles_obj.obstacles

    def colided_line(self, visLine: list, collideLine: list):
        intersectPoint = intersect_point(visLine, collideLine)
        if intersectPoint == [-1, -1]:
            return visLine

        return [visLine[0], intersectPoint]


    def is_collided(self, point_ind):
        return self.collidedPoints[point_ind]


    def vision(self):
        angle1 = self.angle - self.visionAngle / 2
        angle2 = self.angle + self.visionAngle / 2

        visionPolyPoints = []
        self.collidedPoints.clear()

        for angle in numpy.arange(angle1, angle2, self.visionFrequency):
            startPoint = self.pos
            endPoint = [self.pos[0] + math.cos(angle) * self.visionRadius,
                        self.pos[1] - math.sin(angle) * self.visionRadius]
            # pygame.draw.aaline(screen, VISION_COLOR, startPoint, endPoint)

            is_collided = False

            visLine = [startPoint, endPoint]
            for obstacle in self.obstacles:
                for edge in obstacle.edges:
                    visLine = self.colided_line(visLine, edge)

            if self.visionRadius > round(line_len(visLine), 3):
                is_collided = True

            self.collidedPoints.append(is_collided)
            visionPolyPoints.append(visLine[1])

        startPoint = [self.pos[0] + math.cos(angle1) * self.size,
                      self.pos[1] - math.sin(angle1) * self.size]
        endPoint = [self.pos[0] + math.cos(angle1) * self.visionRadius,
                    self.pos[1] - math.sin(angle1) * self.visionRadius]
        # pygame.draw.aaline(screen, BLACK, startPoint, endPoint)
        startPoint = [self.pos[0] + math.cos(angle2) * self.size,
                      self.pos[1] - math.sin(angle2) * self.size]
        endPoint = [self.pos[0] + math.cos(angle2) * self.visionRadius,
                    self.pos[1] - math.sin(angle2) * self.visionRadius]
        # pygame.draw.aaline(screen, BLACK, startPoint, endPoint)


        self.visionPoints = visionPolyPoints


    def show(self):


        visionPolyPoints = copy.deepcopy(self.visionPoints)
        visionPolyPoints.append(self.pos)

        pygame.draw.polygon(screen, VISION_COLOR, visionPolyPoints)
        pygame.draw.aalines(screen, VISION_COLOR, True, visionPolyPoints)


        pygame.draw.circle(screen, DARK_RED, self.pos, self.size)       #PLAYER
        pygame.draw.circle(screen, PINK, self.pos, self.size * 0.8)




    def movements(self):

        collision_lines = []
        collision_lines_angles = []

        # for angle in numpy.arange(self.angle, self.angle + 2 * math.pi, self.collisionFrequency):
        #     startPoint = [self.pos[0] + math.cos(angle) * self.size,
        #                   self.pos[1] - math.sin(angle) * self.size]
        #     endPoint = [self.pos[0] + math.cos(angle) * self.collisionRadius,
        #                 self.pos[1] - math.sin(angle) * self.collisionRadius]
        #     # pygame.draw.aaline(screen, BLACK, startPoint, endPoint)        # ЛИНИИ КОЛЛИЗИИ
        #     collision_lines.append([startPoint, endPoint])
        #     collision_lines_angles.append(angle)
        #
        # for ind, line in enumerate(collision_lines):
        #     for obstacle in self.obstacles:
        #         for edge in obstacle.edges:
        #             if is_intersected(line, edge):
        #                 move_angle = collision_lines_angles[ind]
        #                 self.pos[0] += self.moveSpeed * math.cos(move_angle + math.pi)
        #                 self.pos[1] -= self.moveSpeed * math.sin(move_angle + math.pi)


        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.pos[0] += self.moveSpeed * math.cos(self.angle)
            self.pos[1] -= self.moveSpeed * math.sin(self.angle)
        if key[pygame.K_s]:
            self.pos[0] -= self.moveSpeed * math.cos(self.angle)
            self.pos[1] += self.moveSpeed * math.sin(self.angle)
        if key[pygame.K_a]:
            self.pos[0] += self.moveSpeed * math.cos(self.angle + radians(90))
            self.pos[1] -= self.moveSpeed * math.sin(self.angle + radians(90))
        if key[pygame.K_d]:
            self.pos[0] += self.moveSpeed * math.cos(self.angle - radians(90))
            self.pos[1] -= self.moveSpeed * math.sin(self.angle - radians(90))


        new_pos = pygame.mouse.get_pos()
        x_diff = new_pos[0] - self.mx
        y_diff = new_pos[1] - self.my
        self.mx, self.my = pygame.mouse.get_pos()







        self.angle -= radians(self.rotateSpeed * x_diff)





