"""CLASS FallingLetter

    INITIALIZE
        Choose or receive a letter character
        Receive a horizontal position
        Set starting vertical position at the top
        Set falling speed

    METHOD move
        Increase vertical position based on speed

    METHOD matches_key
        Check whether pressed key matches this letter

    METHOD has_reached_bottom
        Check whether letter reached danger bar

    METHOD draw
        Display letter at its current position

END CLASS"""

import random
from typing import Text


class FallingLetters:

    def __init__(self,x, y, height, speed = 100):
        self.letters = random.choice(self.letters)
        self.x = x
        self.y = y
        self.screen_height = height
        self.speed = speed


    def update(self, dt, keys = None):
        if self.active and not self.selected:
            self.y += self.speed * dt

    def intiailPosition(self):
        return (self.x,self.y)

    def reachedBottom(self):
       return self.y >= self.screen_height


    def draw(self,surface):
        if self.active:
            text = Text(self.letters, self.x,self.y)

            if self.selected:
                text.setColor((255,255,0))
            else:
                text.setColor((0,255,0))

            text.draw(surface)