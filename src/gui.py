from __future__ import division
from gevent import spawn, joinall, sleep
import pygame

class Gui(object):
    '''
    Instanciate GUI, passing in table object and width and height dimensions
    '''
    def __init__(self, tbl, width=400, height=800):
        pygame.init()
        pygame.display.set_caption('Pool Sim')
        self.running = False

        self.tbl = tbl
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        self.colors = {}
        self.colors['GREEN'] = (0, 255, 0)
        self.colors['RED'] = (255, 0, 0)

        self.x_scale = self.width / self.tbl.width
        self.y_scale = self.height / self.tbl.length
        self.b_radius = self.tbl.b_radius * min(self.x_scale, self.y_scale)

    def start(self):
        self.running = True
        self.draw_static()
        joinall([spawn(self.update_table), spawn(self.gui_loop)])

    def gui_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
            self.draw_static()
            sleep(1/60)
 

    def draw_static(self):
        self.screen.fill(self.colors['GREEN'])
    
        for ball in self.tbl.balls:
            pygame.draw.circle(self.screen, self.colors['RED'],
                               (int(ball.x_pos * self.x_scale),
                                int(ball.y_pos * self.y_scale)),
                               int(self.b_radius))
    
        pygame.display.flip()


    def update_table(self):
        while not self.running:
            sleep(1)
        while self.running:
            sleep(1/60)
            pass
