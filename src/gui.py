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
        self.colors['GREY'] = (127, 127, 127)

        self.x_scale = self.width / self.tbl.width
        self.y_scale = self.height / self.tbl.length
        self.b_scale = min(self.x_scale, self.y_scale)
        self.b_radius = self.tbl.b_radius * self.b_scale

    def start(self):
        self.running = True
        self.draw_static()
        joinall([spawn(self.gui_loop)])

    def gui_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
            self.draw_static()
            sleep(1/120)


    def _draw_balls(self):
        for ball in self.tbl.balls:
            if ball.active:
                pygame.draw.circle(self.screen, self.colors['RED'],
                                   (int(ball.x_pos * self.x_scale),
                                    int(ball.y_pos * self.y_scale)),
                                   int(self.b_radius))


    def _draw_pockets(self):
        x_positions = [self.tbl.pocket_offset,
                       (self.tbl.width - self.tbl.pocket_offset)]
        y_positions = [self.tbl.pocket_offset,
                       (self.tbl.length/2),
                       (self.tbl.length - self.tbl.pocket_offset)]
        for x_pos in x_positions:
            for y_pos in y_positions:
                pygame.draw.circle(self.screen, self.colors['GREY'],
                                   (int(x_pos * self.x_scale),
                                    int(y_pos * self.y_scale)),
                                   int(self.tbl.pocket_radius * self.b_scale))


    def draw_static(self):
        self.screen.fill(self.colors['GREEN'])
        self._draw_pockets()
        self._draw_balls()

        pygame.display.flip()


    def update_table(self):
        while not self.running:
            sleep(1)
        while self.running:
            sleep(1/60)
            pass
