import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("lightpink")
pygame.display.update()

class Rectangle():
    def __init__(self, color, dimension):
        self.color=color
        self.surface=screen
        self.rectdimension=dimension
    def draw(self):
        self.drawrect=pygame.draw.rect(self.surface, self.color, self.rectdimension)

yellowrect=Rectangle("yellow", (100,200, 50, 70))
yellowrect.draw()
bluerect=Rectangle("skyblue", (200,200, 180, 170))
bluerect.draw()
orangerect=Rectangle("orange", (500,500, 90, 80))
orangerect.draw()

pygame.display.update()
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            break
pygame.quit()