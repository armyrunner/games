
import time, string
from text import Text

class ScoreBoard:

    def __init__(self, x, y, width, height):
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
        green = (0, 255, 0)

        score = self.getScore()
        leftside = f"POINTS: {score}" 
        LeftArea = Text(leftside,(self.screen_width*.05), self.y)
        LeftArea.setColor(green)
        LeftArea.draw(surface)

        elapsedTime = self.getTimer()
        middle = f"TIMER: {elapsedTime:.2f}"
        MiddleArea = Text(middle, self.screen_width*.20, self.y)
        MiddleArea.setColor(green)
        MiddleArea.draw(surface)

        rightside = (self.letters)
        RightArea = Text(rightside, self.screen_width *.65, self.y)
        RightArea.setColor(green)
        RightArea.draw(surface)
        