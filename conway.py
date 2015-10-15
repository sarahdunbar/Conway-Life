"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Cubey(Sprite):
    def __init__(self, position):

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        life = Color(0xeeff00, 1.0)
        norm = Color(0x872657, 1.0)
        whiwhi = Color(0xFFFFFF, 1.0)
        lifeline = LineStyle (1, life)
        repline = LineStyle (1, norm)
        whiteline = LineStyle (1, whiwhi)
        deadark = RectangleAsset(5, 5, whiteline, whiwhi)

    def step(self):
        for cw in self.getSpritesbyClass(Cubey):
            cw.step()

[0] * 10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

myapp = Conway()
myapp.run()

