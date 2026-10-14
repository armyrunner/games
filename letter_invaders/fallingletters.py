import pygame
import random
from text import Text


class FallingLetters:

    def __init__(self,letters,x, y, height, speed = 5):
        self.letters = random.choice(letters)
        self.x = x
        self.y = y
        self.screen_height = height
        self.speed = speed

        self.active = True
        self.selected = False


    def update(self, dt, keys = None):
        if self.active and not self.selected:
            self.y += self.speed * dt

    def intialPosition(self):
        return (self.x,self.y)

    def reachBottom(self):
       return self.y >= self.screen_height


    def draw(self,surface):
        if self.active:
            font = pygame.font.Font(None, 36)
            image = font.render(self.letters, True, (0, 255, 0))
            surface.blit(image, (self.x, self.y))
        # if self.active:
        #     text = Text(self.letters, self.x,self.y)

        #     if self.selected:
        #         text.setColor((255,255,0))
        #     else:
        #         text.setColor((0,255,0))

        #     text.draw(surface)