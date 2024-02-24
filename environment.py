import pygame

class Environment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=1)
        #self.screen = pygame.display.set_mode((500, 500), vsync=1)
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.w,self.h = self.screen.get_size()
        self.dt = 0
        self.framerate = 200
        self.bg_color = (0,0,0)
        self.objects = []
        self.game_over = False
            
    def clock_tick(self):
        self.dt = self.clock.tick(self.framerate) / 1000
    
    def update(self, difficulty):
        for i in self.objects:
            i.update(self.dt, self.w, self.h, difficulty)
    
    def draw(self):
        self.screen.fill(self.bg_color)
        for i in self.objects:
            i.draw(self.screen, self.w, self.h)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
    
