import numpy as np

def calculate_intercept_point(velocity_target, lead_time, acceleration_intercept):
	x_lead = velocity_target * lead_time
	coeffs = [0.5 * acceleration_intercept, -velocity_target, -x_lead]
	roots = np.roots(coeffs)
	time_intercept = [r for r in roots if r > 0][0]
	x_intercept = 0.5 * acceleration_intercept * (time_intercept**2)
	velocity_interceptor = acceleration_intercept * time_intercept
	return time_intercept, x_intercept, velocity_interceptor

def simulate_ballistic_reentry(y0=480.0, v0=240.0, angle_deg=53.13, g=9.8, dt=0.001):
	rad = np.radians(angle_deg)
	state = np.array([0.0, y0, v0 * np.cos(rad), v0 * np.sin(rad)])
	trajectory = [state.copy()]
	t = 0.0
	while state[1] >= 0.0:
		state[0] += state[2] * dt
		state[1] += state[3] * dt
		state[3] -= g * dt
		t += dt
		trajectory.append(state.copy())
	return t, np.array(trajectory)
