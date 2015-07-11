from ball import Ball
from physics import *
from math import copysign, sqrt, atan, sin, cos, pi

from gevent import sleep

class Table(object):
    def __init__(self, table_data, shots_sequence):
        self.width = table_data['width']
        self.length = table_data['length']
        self.b_radius = table_data['b_radius']
        self.alpha = table_data['alpha']
        self.dt = table_data['dt']
        self.vel_thres = table_data['vel_threshold']
        self.num_shots = int(table_data['num_shots'])

        self.pocket_radius = table_data['pocket_radius']
        self.pocket_offset = table_data['pocket_offset']

        self.balls = []
        self.total_score = 0

        self.add_ball(self.width/2, self.length/2, 0)
        self.balls[0].active = False

        for ball in table_data['balls']:
            self.add_ball(*ball)

        self.shots_sequence = shots_sequence

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
        print "Ball sunk! score => %d" % self.total_score

    def loop(self):
        for shot in self.shots_sequence:
            # set shot velocities
            self.balls[0].x_vel = shot[0]
            self.balls[0].y_vel = shot[1]

            # if previous shot => scratch, find valid whiteball position
            if self.balls[0].active == False:
                self.balls[0].active = True
                self.balls[0].x_pos = shot[2]
                self.balls[0].y_pos = shot[3]
                valid_reset = False
                while valid_reset == False:
                    valid_reset = True
                    for ball in self.balls[1:]:
                        if check_collision(self.balls[0].x_pos, self.balls[0].y_pos, self.b_radius,
                                           ball.x_pos, ball.y_pos, self.b_radius):
                            valid_reset = False
                            # edge case if the ball is RIGHT on top
                            if (ball.x_pos == self.balls[0].x_pos and
                                ball.y_pos == self.balls[0].y_pos):
                                #very stupid solution
                                ball.y_pos -= 1
                            else:
                                nx = ball.x_pos - self.balls[0].x_pos
                                ny = ball.y_pos - self.balls[0].y_pos
                                if nx == 0:
                                    pheta = pi/2
                                else:
                                    pheta = atan(ny/nx)
                                dist = sqrt(nx ** 2 + ny ** 2)
                                d = 2*self.b_radius - dist
                                self.balls[0].x_pos -= d*cos(pheta)
                                self.balls[0].y_pos -= d*sin(pheta)

            shot_running = True
            while shot_running:
                shot_running = False

                # update position, vel, accel
                for ball in self.balls:
                    if not ball.active: continue

                    ball.x_pos += ball.x_vel*self.dt
                    ball.y_pos += ball.y_vel*self.dt

                    ball.x_acc = (-1)*copysign(1,ball.x_vel)*(ball.x_vel ** 2)*self.alpha
                    ball.y_acc = (-1)*copysign(1,ball.y_vel)*(ball.y_vel ** 2)*self.alpha

                    if abs(ball.x_acc*self.dt) <= abs(ball.x_vel):
                        ball.x_vel += ball.x_acc*self.dt
                    else:
                        ball.x_vel = 0
                        ball.x_acc = 0

                    if abs(ball.y_acc*self.dt) <= abs(ball.y_vel):
                        ball.y_vel += ball.y_acc*self.dt
                    else:
                        ball.y_vel = 0
                        ball.y_acc = 0

                    if shot_running == False:
                        if abs(ball.x_vel) > self.vel_thres or abs(ball.y_vel) > self.vel_thres:
                            shot_running = True

                    ball.check_collision_table()
                    ball.check_collision_pocket()

                # balls_to_check = self.balls[:]

                # #check collision
                # for ball in balls_to_check:
                #     balls_to_check.remove(ball)
                #     if not ball.active:
                #         continue

                #     for b_other in balls_to_check:
                #         if not b_other.active:
                #             continue
                #         ball.check_collision(b_other)
                for ball in self.balls:
                    if ball.active == False: continue
                    for ball2 in self.balls:
                        if ball2.active == False: continue
                        if ball != ball2:
                            ball.check_collision(ball2)

                sleep(self.dt*0.0001)
            print "stopping"
            for ball in self.balls:
                ball.x_vel = 0
                ball.y_vel = 0

