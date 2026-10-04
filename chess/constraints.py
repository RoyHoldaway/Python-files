import pygame
class Constraints:
    def __init__(self):
        self.width = 640
        self.height = 640
        self.cell_size = 80
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Chess.py")
        self.clock = pygame.time.Clock()
        pygame.init()