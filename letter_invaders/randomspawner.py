
import random
from fallingletters import *

class RandomSpawner:

    def __init__(self,letters,width,height):
        self.letters = letters
        self.screen_width = width
        self.screen_height = height

        self.failing_letters = []


    def spawn(self):
        randomLetter = random.randint(20,self.screen_width - 20)

        letter = FallingLetters(self.letters,randomLetter,0,self.screen_height)

        self.failing_letters.append(letter)
        
    def update(self,dt):
        for letter in self.failing_letters[:]:
            letter.update(dt)

            if letter.reachBottom() or letter.selected:
                self.failing_letters.remove(letter)
    
    def draw(self, surface):
        for letter in self.failing_letters:
            letter.draw(surface)