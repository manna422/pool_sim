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
        pocket_rad = self.table.pocket_radius
        pocket_offset = self.table.pocket_offset

        # bottom left
        pocket_x = pocket_offset 
        pocket_y = pocket_offset
        if (check_collision(self.x_pos, self.y_pos,
            self.table.b_radius, pocket_x, pocket_y,
            pocket_rad)):
            self.table.remove_ball(self)

        # bottom center
        pocket_x = self.table.length // 2
        if (check_collision(self.x_pos, self.y_pos,
            self.table.b_radius, pocket_x, pocket_y,
            pocket_rad)):
            self.table.remove_ball(self)

        # bottom left
        pocket_x = self.table.length - pocket_offset
        if (check_collision(self.x_pos, self.y_pos,
            self.table.b_radius, pocket_x, pocket_y,
            pocket_rad)):
            self.table.remove_ball(self)

        # top right
        pocket_y = self.table.width - pocket_offset
        if (check_collision(self.x_pos, self.y_pos,
            self.table_b_radius, pocket_x, pocket_y,
            pocket_rad)):
            self.table.remove_ball(self)

        # top center
        pocket_x = self.table.length // 2
        if (check_collision(self.x_pos, self.y_pos,
            self.table_b_radius, pocket_x, pocket_y,
            pocket_rad):
            self.table.remove_ball(self)

        # top left
        pocket_x = pocket_offset
        if (check_collision(self.x_pos, self.y_pos,
            self.table_b_radius, pocket_x, pocket_y,
            pocket_rad)):
            self.table.remove_ball(self)


