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
	# hard code mass as 1 for now
	a_mass = 1
	b_mass = 1

	a.x_vel, b.x_vel = (((a.x_vel * (a_mass - b_mass) + (2 * b_mass * b.x_vel)) / (a_mass + b_mass)),
						((b.x_vel * (b_mass - a_mass) + (2 * a_mass * a.x_vel)) / (a_mass + b_mass)))
	a.y_vel, b.y_vel = (((a.y_vel * (a_mass - b_mass) + (2 * b_mass * b.y_vel)) / (a_mass + b_mass)),
						((b.y_vel * (b_mass - a_mass) + (2 * a_mass * a.y_vel)) / (a_mass + b_mass)))


def table_collision(tbl, ball):
	if ((ball.x_pos - tbl.b_radius) < 0) or ((ball.x_pos + tbl.b_radius) > tbl.width):
		ball.x_vel *= -1
		ball.x_pos += ball.x_pos*tbl.dt
	if ((ball.y_pos - tbl.b_radius) < 0) or ((ball.y_pos + tbl.b_radius) > tbl.length):
		ball.y_vel *= -1
		ball.y_pos += ball.y_pos*tbl.dt