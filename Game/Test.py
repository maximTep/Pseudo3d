import pygame
import math

pygame.init()
pygame.font.init()
screenWidth = 900
screenHeight = 650
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Lab")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255, 50)  # This color contains an extra integer. It's the alpha value.
PURPLE = (255, 0, 255)


def colide_point(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return [x, y]

def dist(p1: list, p2: list):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def scal(vec1, vec2):
    return vec1[0]*vec2[0] + vec1[1]*vec2[1]

running = True
cnt = 0
lines = []
points = []
bises = []
newPoints = []
done = False
while running:



    pygame.event.pump()
    pygame.time.delay(33)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            #print(1)
            if cnt < 4:
                cnt += 1
                points.append([mx, my])
            elif cnt == 3:
                pygame.draw.aalines(screen, BLACK, True, points)
                cnt = 4

                lines.append([points[0], points[1]])
                lines.append([points[1], points[2]])
                lines.append([points[2], points[3]])
                lines.append([points[3], points[0]])
                print(lines)


    for point in points:
        pygame.draw.circle(screen, BLACK, [point[0], point[1]], 2)
    if cnt == 4:
        oop = 1
        try:
            pygame.draw.aalines(screen, BLACK, True, points)
            if not done:

                lines.clear()
                lines.append([points[0], points[1]])
                lines.append([points[1], points[2]])
                lines.append([points[2], points[3]])
                lines.append([points[3], points[0]])

                for i in range(4):
                    if i == 0:
                        vec1 = [points[i+1][0] - points[i][0], points[i+1][1] - points[i][1]]
                        vec2 = [points[-1][0] - points[i][0], points[-1][1] - points[i][1]]
                        cosa = scal(vec1, vec2) / (dist(points[i+1], points[i]) * dist(points[-1], points[i]))
                        #print(cosa)

                        x = vec2[0]
                        y = vec2[1]
                        angle = math.acos(cosa)
                        cs = math.cos(angle/2)
                        sn = math.sin(angle/2)
                        rx = x * cs - y * sn
                        ry = x * sn + y * cs


                        #pygame.draw.aaline(screen, BLACK, points[i], [points[i][0] + rx, points[i][1] + ry])
                        bis = [points[i], [points[i][0] + rx, points[i][1] + ry]]

                        for ind, line in enumerate(lines):

                            # print(line)
                            interPoint = colide_point(bis, line)
                            # for lin in lines:
                            if interPoint != bis[0]:
                                if (line[0][0] <= interPoint[0] <= line[1][0]) or (
                                        line[0][0] >= interPoint[0] >= line[1][0]):
                                    if (line[0][1] <= interPoint[1] <= line[1][1]) or (
                                            line[0][1] >= interPoint[1] >= line[1][1]):
                                        if dist(bis[0], interPoint) > 10:
                                            # print(dist(bis[0], interPoint))
                                            bises.append([bis[0], interPoint])
                                            newPoints.append(interPoint)
                    elif i != 3:
                        vec1 = [points[i + 1][0] - points[i][0], points[i + 1][1] - points[i][1]]
                        vec2 = [points[i-1][0] - points[i][0], points[i-1][1] - points[i][1]]
                        cosa = scal(vec1, vec2) / (dist(points[i + 1], points[i]) * dist(points[i-1], points[i]))
                        # print(cosa)

                        x = vec2[0]
                        y = vec2[1]
                        angle = math.acos(cosa)
                        cs = math.cos(angle / 2)
                        sn = math.sin(angle / 2)
                        rx = x * cs - y * sn
                        ry = x * sn + y * cs

                        # pygame.draw.aaline(screen, BLACK, points[i], [points[i][0] + rx, points[i][1] + ry])
                        bis = [points[i], [points[i][0] + rx, points[i][1] + ry]]

                        for ind, line in enumerate(lines):

                            # print(line)
                            interPoint = colide_point(bis, line)
                            # for lin in lines:
                            if interPoint != bis[0]:
                                if (line[0][0] <= interPoint[0] <= line[1][0]) or (
                                        line[0][0] >= interPoint[0] >= line[1][0]):
                                    if (line[0][1] <= interPoint[1] <= line[1][1]) or (
                                            line[0][1] >= interPoint[1] >= line[1][1]):
                                        if dist(bis[0], interPoint) > 10:
                                            # print(dist(bis[0], interPoint))
                                            bises.append([bis[0], interPoint])
                                            newPoints.append(interPoint)
                    else:
                        vec1 = [points[0][0] - points[i][0], points[0][1] - points[i][1]]
                        vec2 = [points[i - 1][0] - points[i][0], points[i - 1][1] - points[i][1]]
                        cosa = scal(vec1, vec2) / (dist(points[0], points[i]) * dist(points[i - 1], points[i]))
                        # print(cosa)

                        x = vec2[0]
                        y = vec2[1]
                        angle = math.acos(cosa)
                        cs = math.cos(angle / 2)
                        sn = math.sin(angle / 2)
                        rx = x * cs - y * sn
                        ry = x * sn + y * cs

                        # pygame.draw.aaline(screen, BLACK, points[i], [points[i][0] + rx, points[i][1] + ry])
                        bis = [points[i], [points[i][0] + rx, points[i][1] + ry]]
                        #newPoints.clear()

                        for ind, line in enumerate(lines):

                            # print(line)
                            interPoint = colide_point(bis, line)
                            #for lin in lines:
                            if interPoint != bis[0]:
                                if (line[0][0] <= interPoint[0] <= line[1][0]) or (line[0][0] >= interPoint[0] >= line[1][0]):
                                    if (line[0][1] <= interPoint[1] <= line[1][1]) or (line[0][1] >= interPoint[1] >= line[1][1]):
                                        if dist(bis[0], interPoint) > 10:
                                            #print(dist(bis[0], interPoint))
                                            bises.append([bis[0], interPoint])
                                            newPoints.append(interPoint)
                #print(len(newPoints))
                done = True

            for bise in bises:
                pygame.draw.aaline(screen, GREEN, bise[0], bise[1])
                #pygame.draw.circle(screen, BLACK, bise[1], 10)


            pygame.draw.aalines(screen, RED, True, newPoints)
            #print(len(points))
        except:
            pygame.draw.aalines(screen, BLACK, True, points)
            done = False
            if not done:
                print(1)
                points.reverse()
                lines.clear()
                lines.append([points[0], points[1]])
                lines.append([points[1], points[2]])
                lines.append([points[2], points[3]])
                lines.append([points[3], points[0]])

                for i in range(4):
                    if i == 0:
                        vec1 = [points[i + 1][0] - points[i][0], points[i + 1][1] - points[i][1]]
                        vec2 = [points[-1][0] - points[i][0], points[-1][1] - points[i][1]]
                        cosa = scal(vec1, vec2) / (dist(points[i + 1], points[i]) * dist(points[-1], points[i]))
                        # print(cosa)

                        x = vec2[0]
                        y = vec2[1]
                        angle = math.acos(cosa)
                        cs = math.cos(angle / 2)
                        sn = math.sin(angle / 2)
                        rx = x * cs - y * sn
                        ry = x * sn + y * cs

                        # pygame.draw.aaline(screen, BLACK, points[i], [points[i][0] + rx, points[i][1] + ry])
                        bis = [points[i], [points[i][0] + rx, points[i][1] + ry]]

                        for ind, line in enumerate(lines):

                            # print(line)
                            interPoint = colide_point(bis, line)
                            # for lin in lines:
                            if interPoint != bis[0]:
                                if (line[0][0] <= interPoint[0] <= line[1][0]) or (
                                        line[0][0] >= interPoint[0] >= line[1][0]):
                                    if (line[0][1] <= interPoint[1] <= line[1][1]) or (
                                            line[0][1] >= interPoint[1] >= line[1][1]):
                                        if dist(bis[0], interPoint) > 10:
                                            # print(dist(bis[0], interPoint))
                                            bises.append([bis[0], interPoint])
                                            newPoints.append(interPoint)
                    elif i != 3:
                        vec1 = [points[i + 1][0] - points[i][0], points[i + 1][1] - points[i][1]]
                        vec2 = [points[i - 1][0] - points[i][0], points[i - 1][1] - points[i][1]]
                        cosa = scal(vec1, vec2) / (dist(points[i + 1], points[i]) * dist(points[i - 1], points[i]))
                        # print(cosa)

                        x = vec2[0]
                        y = vec2[1]
                        angle = math.acos(cosa)
                        cs = math.cos(angle / 2)
                        sn = math.sin(angle / 2)
                        rx = x * cs - y * sn
                        ry = x * sn + y * cs

                        # pygame.draw.aaline(screen, BLACK, points[i], [points[i][0] + rx, points[i][1] + ry])
                        bis = [points[i], [points[i][0] + rx, points[i][1] + ry]]

                        for ind, line in enumerate(lines):

                            # print(line)
                            interPoint = colide_point(bis, line)
                            # for lin in lines:
                            if interPoint != bis[0]:
                                if (line[0][0] <= interPoint[0] <= line[1][0]) or (
                                        line[0][0] >= interPoint[0] >= line[1][0]):
                                    if (line[0][1] <= interPoint[1] <= line[1][1]) or (
                                            line[0][1] >= interPoint[1] >= line[1][1]):
                                        if dist(bis[0], interPoint) > 10:
                                            # print(dist(bis[0], interPoint))
                                            bises.append([bis[0], interPoint])
                                            newPoints.append(interPoint)
                    else:
                        vec1 = [points[0][0] - points[i][0], points[0][1] - points[i][1]]
                        vec2 = [points[i - 1][0] - points[i][0], points[i - 1][1] - points[i][1]]
                        cosa = scal(vec1, vec2) / (dist(points[0], points[i]) * dist(points[i - 1], points[i]))
                        # print(cosa)

                        x = vec2[0]
                        y = vec2[1]
                        angle = math.acos(cosa)
                        cs = math.cos(angle / 2)
                        sn = math.sin(angle / 2)
                        rx = x * cs - y * sn
                        ry = x * sn + y * cs

                        # pygame.draw.aaline(screen, BLACK, points[i], [points[i][0] + rx, points[i][1] + ry])
                        bis = [points[i], [points[i][0] + rx, points[i][1] + ry]]
                        # newPoints.clear()

                        for ind, line in enumerate(lines):

                            # print(line)
                            interPoint = colide_point(bis, line)
                            # for lin in lines:
                            if interPoint != bis[0]:
                                if (line[0][0] <= interPoint[0] <= line[1][0]) or (
                                        line[0][0] >= interPoint[0] >= line[1][0]):
                                    if (line[0][1] <= interPoint[1] <= line[1][1]) or (
                                            line[0][1] >= interPoint[1] >= line[1][1]):
                                        if dist(bis[0], interPoint) > 10:
                                            # print(dist(bis[0], interPoint))
                                            bises.append([bis[0], interPoint])
                                            newPoints.append(interPoint)
                # print(len(newPoints))
                done = True

            for bise in bises:
                pygame.draw.aaline(screen, GREEN, bise[0], bise[1])
                # pygame.draw.circle(screen, BLACK, bise[1], 10)

            pygame.draw.aalines(screen, RED, True, newPoints)
            # print(len(points))



    pygame.display.update()



pygame.quit()

