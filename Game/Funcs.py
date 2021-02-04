from PGinit import *
import pygame
import math



def radians(grades: float):
    return grades * math.pi / 180


def scal(vec1, vec2):
    return vec1[0]*vec2[0] + vec1[1]*vec2[1]


def get_angle(line1, line2=None):
    if line2 is None:
        line2 = [[0, 0], [10, 0]]
    vec1 = [line1[1][0] - line1[0][0], line1[1][1] - line1[0][1]]
    vec2 = [line2[1][0] - line2[0][0], line2[1][1] - line2[0][1]]
    cosa = scal(vec1, vec2) / (dist(line1[0], line1[1]) * dist(line2[0], line2[1]))
    angle = math.acos(cosa)
    return angle


def is_intersected(segment1, segment2):
    def area(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def intersect_1(a, b, c, d):
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return max(a, c) <= min(b, d)

    a = segment1[0]
    b = segment1[1]
    c = segment2[0]
    d = segment2[1]
    return intersect_1(a[0], b[0], c[0], d[0]) and intersect_1(a[1], b[1], c[1], d[1]) and area(a, b, c) * area(a, b, d) <= 0 and area(c, d, a) * area(c, d, b) <= 0


def intersect_point(line1, line2):
    if not is_intersected(line1, line2):
        return [-1, -1]
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return [-1, -1]

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return [x, y]


def dist(p1: list, p2: list):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def line_len(line: list):
    return dist(line[0], line[1])

