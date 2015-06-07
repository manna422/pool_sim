from ball import Ball
from physics import *

from gevent import sleep

class Table(object):
    def __init__(self, width, length, b_radius,
        pocket_radius, pocket_offset):
        self.width = width
        self.length = length
        self.b_radius = b_radius
        self.balls = []

        self.pocket_radius = pocket_radius
        self.pocket_offset = pocket_offset

        self.total_score = 0

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

    def remove_ball(self, ball):
        self.total_score += ball.score
        ball.active = False

    def loop(self):
        dt = 0.1
        alpha = 0.000001

        #test
        self.balls[0].x_vel = 100
        self.balls[0].y_vel = 200

        while True:
            # update position, vel, accel
            for ball in self.balls:
                if not ball.active: continue
                ball.x_pos += ball.x_vel*dt
                ball.y_pos += ball.y_vel*dt

                ball.x_vel += ball.x_acc*dt
                ball.y_vel += ball.y_acc*dt

                ball.x_acc = (-1)*(ball.x_vel ** 2)*alpha
                ball.y_acc = (-1)*(ball.y_vel ** 2)*alpha

            balls_to_check = self.balls[:]

            #check collision
            for ball in balls_to_check:
                balls_to_check.remove(ball)
                if not ball.active:
                    continue

                ball.check_collision_table()
                ball.check_collision_pocket()

                for b_other in balls_to_check:
                    if not b_other.active:
                        continue
                    ball.check_collision(b_other)

            print "x: %d y: %d" % (self.balls[0].x_pos, self.balls[0].y_pos)
            sleep(dt)