"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

"""
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
"""

norm = Color(0x872657, 1.0)
repline = LineStyle (1, norm)
deadark = RectangleAsset(5, 5, repline, norm)
for x in range(21):
    j = 1
    for y in range(21):
        Sprite(deadark, (5*x, 5*y))
for x in range(21, 42):
    j = 1
    for y in range(21):
        Sprite(deadark, (5*x, 5*y))


myapp = App()
myapp.run()

