import pygame


class DangerBar:

    GREEN = (0,255,0)
    YELLOW = (255,255,0)
    RED = (255,0,0)
    EMPTY = None

    def __init__(self, width, height, cell_width):
        self.screen_width = width
        self.screen_height = height

        self.cell_width = max(1,cell_width)
        self.bar_height = 15
        self.bar_y = height - self.bar_height

        num_cell = (width + cell_width - 1) // self.cell_width
        self.cells = [self.GREEN] * num_cell

        self.game_over = False


    def hit(self,x):
        index = int(x // self.cell_width)

        if index < 0 or index >= len(self.cells):
            return
        
        if self.cells[index] is self.EMPTY:
            self.game_over = True
            return
        
        if self.cells[index] == self.GREEN:
            self.cells[index] = self.YELLOW
        elif self.cells[index] == self.YELLOW:
            self.cells[index] = self.RED
        elif self.cells[index] == self.RED:
            self.cells[index] = self.EMPTY
        
    def draw(self, surface):
        for index, color in enumerate(self.cells):
            if color is not self.EMPTY:
                x = index * self.cell_width
                cell_width = min(self.cell_width - 1, self.screen_width - x)
                pygame.draw.rect(surface,color,
                                 (x,self.bar_y,self.cell_width,self.bar_height))