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

class FALLINGLETTERS:

    def __init__(self,letters, x, y, speed, dx, dy, width,height):
        self.letters = letters
        self.x = x
        self.y = y
        self.speed = speed
        self.dx = dx
        self.dy = dy
        self.screen_width = width
        self.screen_height = height


    def move(self):
        pass


    def intiailPosition(self):
        return (self.x,self.y)

    def reachedBotton(self):
        if self.y >= self.screen_height:
            return True
        return False 

    def draw(self):
        pass
