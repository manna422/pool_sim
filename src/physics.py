from math import sqrt, sin, cos, pi

def check_collision(ax, ay, a_radius, bx, by, b_radius):
	if (sqrt(pow((ax - bx), 2) + pow((ay - by), 2)) <
		(a_radius + b_radius)):
		return True
	else:
		return False

def check_collision_table(tbl, x_pos, y_pos):
	if (((x_pos - tbl.b_radius) < 0)
        or ((x_pos + tbl.b_radius) > tbl.width)
        or ((y_pos - tbl.b_radius) < 0)
        or ((y_pos + tbl.b_radius) > tbl.length)):
		return True
	else:
		return False

def ball_collision(a, b):
	d = sqrt(pow((a.x_pos - b.x_pos), 2) + pow((a.y_pos - b.y_pos), 2))
	nx = (b.x_pos - a.x_pos) / d
	ny = (b.y_pos - a.y_pos) / d
	p = (2 * (a.x_vel * nx + a.y_vel * ny - b.x_vel * nx - b.y_vel * ny) /
		(a.mass + b.mass))
	a.x_vel = a.x_vel - p * a.mass * nx
	a.y_vel = a.y_vel - p * a.mass * ny
	b.x_vel = b.x_vel + p * b.mass * nx
	b.y_vel = b.y_vel + p * b.mass * ny


def table_collision(tbl, ball):
	if ((ball.x_pos - tbl.b_radius) < 0) or ((ball.x_pos + tbl.b_radius) > tbl.width):
		ball.x_vel *= -1
		ball.x_pos += ball.x_pos*tbl.dt
	if ((ball.y_pos - tbl.b_radius) < 0) or ((ball.y_pos + tbl.b_radius) > tbl.length):
		ball.y_vel *= -1
		ball.y_pos += ball.y_pos*tbl.dt
