#
# You should not need to edit this file.
#
import pygame
import pygame.locals


class Game:
    def __init__( self, name, width, height, frames_per_second ):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True
        self.delta_time = 0.0
        
        self.screen = pygame.display.set_mode(
                # set the size
                ( width, height ),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA)

        # set the title of the window
        pygame.display.set_caption( name )
        
        # set time tracking
        self.clock = pygame.time.Clock( )
        self.this_frame_time = pygame.time.get_ticks( ) / 1000.
        self.last_frame_time = self.this_frame_time
        return

    def get_frame_time( self ):
        return self.this_frame_time
        
    def get_delta_time( self ):
        return self.delta_time
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        self.spawn.update(dt)
        return

    def paint(self, surface):
        self.spawn.draw(surface)
        self.score_board.draw(surface)
        return

    def main_loop( self ):
        keys = set( )
        buttons = set( )
        mouse_position = ( 1, 1 )
        self.last_frame_time = pygame.time.get_ticks( ) / 1000.

        falling_letters = []

        while True:
            
            self.clock.tick( self.frames_per_second )
            newkeys = set( )
            newbuttons = set( )

            for e in pygame.event.get( ):
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    
                    char = e.unicode.upper()

                    if char and char.isprintable():
                        print("key pressed: ", char)

                    for letters in falling_letters:
                        if letters.active and letters.char == char:
                            letters.selected = True
                            letters.active = False
                            self.score_board.getScore += 1
                            break

                    self.this_frame_time = pygame.time.get_ticks / 1000
                    self.delta_time = self.this_frame_time - self.last_frame_time
                    self.this_frame_time = self.this_frame_time

                    for letters in falling_letters[:]:
                        letters.update()

                        if not letters.active or letters.y > self.height:
                            falling_letters.remove(letters)

            if self.on:
                self.screen.fill((0,0,0))
                self.game_logic( keys, newkeys, buttons,
                                newbuttons, mouse_position, self.delta_time )
                self.paint( self.screen )

            pygame.display.flip( )
        return