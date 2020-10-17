import pygame as pg
import numpy as np
import time
import math

(WIDTH, HEIGHT) = (800, 800)
IN_ROW = 10
IN_COL = 10
TOTAL = IN_ROW * IN_COL
START = (IN_ROW - 1, 0)
WIN_STATE = (0, IN_COL - 1)
LOSE_STATE = (1, IN_COL - 1)


class GridWorld:
    def __init__(self, width, height, numOfRects):
        self.sizeOfRect = self.states
        self.numOfRects = numOfRects
        self.rectMatrix = self.getRectMatrix()

    def getRectMatrix(self):
        rectMatrix = []
        tempRectMatrix = []
        for i in range(self.numOfRects):
            for j in range(self.numOfRects):
                tempRect = pg.Rect(
                    i * self.sizeOfRect, j * self.sizeOfRect, self.sizeOfRect, self.sizeOfRect)
                tempRectMatrix.append(tempRect)
            rectMatrix.append(tempRectMatrix)
            tempRectMatrix = []
        return rectMatrix


class State:
    def __init__(self, state=START):
        self.board = np.zeros([IN_ROW, IN_COL], dtype=int)
        self.state = state
        self.isEnd = False

    def getReward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return 0


def main():
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.get_surface().fill((255, 255, 255))
    running = True

    gridWorld = GridWorld(WIDTH, HEIGHT, 10)

    while running:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
        pg.display.update()

    pg.quit()


# main()
print(np.zeros([IN_COL, IN_ROW], dtype=int))
