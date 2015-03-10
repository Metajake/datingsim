import pygame

class Graphics(object):
    def __init__(self):
        pass
        
    def initialize(self):
        pygame.init()
        self.make_screen()
        
    def make_screen(self):
        size = width,height = 800,600
        screen = pygame.display.set_mode(size)