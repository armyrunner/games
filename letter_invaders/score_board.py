
import time, string
from text import Text

class ScoreBoard:

    def __init__(self, x,y,width, height):
        self.x = x
        self.y = y
        self.screen_width = width
        self.screen_height = height
        
        self.score = 0
        self.timer = time.perf_counter()
        self.letters = (string.ascii_uppercase + string.digits + string.punctuation)

    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getWidth(self):
        return self.screen_width
    
    def getHeight(self):
        return self.screen_height
    
    def getScore(self):
        return self.score
    
    def getTimer(self):
        return time.perf_counter() - self.timer
    
    def getLetters(self):
        return self.letters
    
    def draw(self,surface):
        leftside = "POINTS: " + str(self.score)
        LeftArea = Text(leftside, self.x*.5, self.y)
        LeftArea.setColor((0,255,0))
        LeftArea.draw(surface)

        elapsed = self.getTimer()
        middle = "TIMER:  + {elapsed:.1f}"
        MiddleArea = Text(middle, 300, 20)
        MiddleArea.setColor((0,255,0))
        MiddleArea.draw(surface)

        rightside = " ".join(self.letters)
        RightArea = Text(rightside, 550)
        RightArea.setColor((0,255,0))
        RightArea.draw(surface)
        