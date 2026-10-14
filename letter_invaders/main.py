import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE

from score_board import ScoreBoard
from randomspawner import RandomSpawner
from dangerbar import DangerBar
from text import Text
#from dangerbar import *

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "Letter Invaders"
# pixels width
WINDOW_WIDTH  = 1000
# pixels high
WINDOW_HEIGHT = 800
# frames per second
DESIRED_RATE  = 5

class PygameApp( game.Game):

    def __init__( self, title, width, height, frame_rate ):
        
        game.Game.__init__(self,title, width, height, frame_rate )

        font = pygame.font.Font(None, 20)
        character_width = font.size("A")[0]

        self.score_board = ScoreBoard(15,15, width, height)
        self.danger_bar = DangerBar(width,height,character_width)
        self.spawn = RandomSpawner(self.score_board.letters, width, height,self.danger_bar) 

        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        # keys contains all keys currently held down
        # newkeys contains all keys pressed since the last frame
        # Use pygame.K_? as the keyboard keys.
        # Examples: pygame.K_a, pygame.K_UP, etc.
        # if pygame.K_UP in newkeys:
        #    The user just pressed the UP key
        #
        # buttons contains all mouse buttons currently held down
        # newbuttons contains all buttons pressed since the last frame
        # Use 1, 2, 3 as the mouse buttons
        # if 3 in buttons:
        #    The user is holding down the right mouse button
        #
        # mouse_position contains x and y location of mouse in window
        # dt contains the number of seconds since last frame
        
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        # Update the state of the game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.spawn.update(dt)

        for char in newkeys:

            for letter in self.spawn.falling_letters[:]:
                falling_char = str(letter.letters).upper()
             

                if falling_char == char:

                    letter.selected = True
                    letter.active = False
                    self.spawn.falling_letters.remove(letter)

                    self.score_board.increaseScore()
                    break

                if self.danger_bar.game_over:
                    Text.setText("GAME OVER",)
        

        return
    
    def paint( self, surface ):
        # Draw the current state of the game instance
        self.spawn.draw(surface)
        self.score_board.draw(surface)
        self.danger_bar.draw(surface)

        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )