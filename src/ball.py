from math import sqrt, pow

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
    if (sqrt(pow((self.x_pos - b_other.x_pos), 2)
             + pow((self.y_pos - b_other.y_pos), 2)) <
        (2 * self.table.b_radius)):
        return True
    else:
        return False

def check_collision_table(self):
    #TODO: write function
    pass 
