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