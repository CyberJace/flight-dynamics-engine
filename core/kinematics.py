import numpy as np

def simulate_polynomial_flight(t_max=15.0, dt=0.01):
	t = np.arange(0, t_max, dt)
	x = t**3 - 21*t**2 + 120*t
	y = t**3 - 15*t**2 + 48*t
	vx = 3*t**2 - 42*t + 120
	vy = 3*t**2 - 30*t + 48
	ax = 6*t - 42
	ay = 6*t - 30
	return t, np.array([x, y]), np.array([vx, vy]), np.array([ax, ay])

def simulate_relative_motion(t_max=15.0, dt=0.01):
	t = np.arange(0, t_max, dt)
r_A = np.column_stack((-200 + 20*t, np.zeros_like(t)))
r_B = np.column_stack((np.zeros_like(t), -150 + 15*t))
r_rel = r_A - r_B
dist = np.linalg.norm(r_rel, axis=1)
min_idx = np.argmin(dist)
return t[min_idx], dist[min_idx]
