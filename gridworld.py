import pygame as pg
import time

(sirina, duzina) = (800, 800)


def main():
    pg.init()
    pg.display.set_mode((sirina, duzina))

    running = True

    while running:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
        pg.display.update()

    pg.quit()


main()
