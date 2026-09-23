import numpy as np

def simulate_multistage_burn(stages, x0=0.0, v0=-60.0):
    curr_x = x0
    curr_v = v0
    history = []
    t_global = 0.0
    for duration, accel in stages:
	    dt = 0.01
	    steps = int(duration / dt)
	    for _ in range(steps):
	        curr_x += curr_v * dt + 0.5 * accel * (dt**2)
	        curr_v += accel * dt
	        t_global += dt
	        history.append((t_global, curr_x, curr_v, accel))
    return np.array(history)

def simulate_resistive_motion(m=1000.0, b=200.0, t_max=30.0, dt=0.001):
    t, v = 0.0, 0.0
    v_history, t_history = [], []
    while t <= t_max:
        F_thrust = 3000.0 - 100.0 * t
        F_drag = -b * v
        a = (F_thrust + F_drag) / m
        v += a * dt
        t += dt
        v_history.append(v)
        t_history.append(t)
    v_arr, t_arr = np.array(v_history), np.array(t_history)
    max_idx = np.argmax(v_arr)
    return t_arr{max_idx], v_arr[max_idx]
