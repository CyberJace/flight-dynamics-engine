import numpy as np
from core.kinematics import simulate_polynomial_flight, simulate_relative_motion
from core.propulsion import simulate_multistage_burn, simulate_resistive_motion
from core.interception import calculate_intercept_point, simulate_ballistic_reentry

def main():
    print("		FLIGHT DYNAMICS SIMULATION:		")

    _, r_polynomial, v_polynomial, _ = simulate_polynomial_flight()
    t_min_rel, d_min_rel = simulate_relative_motion()
    print("KINEMATICS -")
    print(f"Closest They Approach (Time): {t_min_rel:.2f} s")
    print(f"Minimum Distance: {d_min_rel:.2f} m\n")

    burn = [(6.0, 20.0), (4.0, 0.0), (10.0, -10.0)]
    thrust = simulate_multistage_burn(burn)
    t_vmax, v_max = simulate_resistive_motion()
    print("PROPULSION AND VEHICLE DYNAMICS -")
    print(f"Multistage Final Position: {thrust[-1, 1]:.2f} m (t={thrust[-1, 0]:.1f}s)")
    print(f"Multistage Final Velocity: {thrust[-1, 2]:.2f} m/s")
    print(f"Highest Speed Point (under drag): {v_max:.2f} m/s (at t={t_vmax:.2f}s)\n")

    t_catch, dist_catch, v_catch = calculate_intercept_point(v_target=40.0, lead_time=15.0, acceleration_intercept=5.0)
    flight_time, ballistic_path = simulate_ballistic_reentry()
    print("BALLISTIC ENTRY -")
    print(f"Time Intercept: {t_catch:.2f} s | Catch Distance: {dist_catch:.2f} m")
    print(f"Ballistic Time: {flight_time:.3f} s")
    print(f"Impact Range  : {ballistic_path[-1, 0]:.2f} m")
    print(f"Impact Speed  : {np.linalg.norm(ballistic_path[-1, 2:]):.2f} m/s\n")

if __name__ == "__main__":
    main()
