from math import sqrt, pow, sin, cos, pi

from physics import *

class Ball(object):
    def __init__(self, table, x_pos, y_pos, score):
        self.table = table
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = 0
        self.y_vel = 0
        self.x_acc = 0
        self.y_acc = 0
        self.score = score

    def check_collision(self, b_other):
        return check_collision(self.x_pos, self.y_pos, 
            self.table.b_radius, b_other.x_pos, b_other.y_pos,
            self.table.b_radius)

    def check_collision_table(self):
        return check_collision_table(self.table, self.x_pos,
            self.y_pos)

    def check_collision_pocket(self):
        pass
        