from ball import Ball

class Table(object):
    def __init__(self, width, length, b_radius):
        self.width = width
        self.length = length
        self.b_radius = b_radius
        self.balls = []

    def add_ball(self, x_pos, y_pos, score):
        # check if bal placed within table contrainsts
        if (((x_pos - self.b_radius) < 0)
            or ((x_pos + self.b_radius) > self.width)
            or ((y_pos - self.b_radius) < 0)
            or ((y_pos + self.b_radius) > self.length)):
            return False

        newBall = Ball(self, x_pos, y_pos, score)
        # check for overlap with other balls
        for existingBall in self.balls:
            if newBall.check_collision(existingBall):
                return False

        self.balls.append(newBall)
        return True
