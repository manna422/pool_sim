from ball import Ball
from physics import *

class Table(object):
    def __init__(self, width, length, b_radius, 
        pocket_radius, pocket_offset):
        self.width = width
        self.length = length
        self.b_radius = b_radius
        self.balls = []

        self.pocket_radius = pocket_radius
        self.pocket_offset = pocket_offset

    def add_ball(self, x_pos, y_pos, score):
        # check if bal placed within table contrainsts
        if check_collision_table(self, x_pos, y_pos):
            return False

        newBall = Ball(self, x_pos, y_pos, score)
        # check for overlap with other balls
        for existingBall in self.balls:
            if newBall.check_collision(existingBall):
                return False

        self.balls.append(newBall)
        return True
