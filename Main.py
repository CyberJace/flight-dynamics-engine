import numpy as np
from core.kinematics import simulate_polynomial_flight, simulate_relative_motion
from core.propulsion import simulate_multistage_burn, simulate_resistive_motion
from core.interception import calculate_intercept_point, simulate_ballistic_reentry

def main():
    print("==================================================")
    print("     FLIGHT DYNAMICS & SIMULATION ENGINE RUN      ")
    print("==================================================\n")

    # 1. Kinematics & Relative Motion
    _, r_poly, v_poly, _ = simulate_polynomial_flight()
    t_min_rel, d_min_rel = simulate_relative_motion()
    print("--- 1. KINEMATICS & RELATIVE NAVIGATION ---")
    print(f"Closest Approach Time : {t_min_rel:.2f} s")
    print(f"Minimum Distance (CPA): {d_min_rel:.2f} m\n")

    # 2. Propulsion & Dynamic Thrust
    burn_profile = [(6.0, 20.0), (4.0, 0.0), (10.0, -10.0)]
    thrust_log = simulate_multistage_burn(burn_profile)
    t_vmax, v_max = simulate_resistive_motion()
    print("--- 2. PROPULSION & VEHICLE DYNAMICS ---")
    print(f"Multistage Final Pos  : {thrust_log[-1, 1]:.2f} m (t={thrust_log[-1, 0]:.1f}s)")
    print(f"Multistage Final Vel  : {thrust_log[-1, 2]:.2f} m/s")
    print(f"Peak Speed Under Drag : {v_max:.2f} m/s (at t={t_vmax:.2f}s)\n")

    # 3. Interception & Entry Mechanics
    t_catch, dist_catch, v_catch = calculate_intercept_point(v_target=40.0, lead_time=15.0, a_interceptor=5.0)
    flight_time, ballistic_path = simulate_ballistic_reentry()
    print("--- 3. GUIDANCE & BALLISTIC REENTRY ---")
    print(f"Pursuit Intercept Time: {t_catch:.2f} s | Catch Distance: {dist_catch:.2f} m")
    print(f"Ballistic Flight Time : {flight_time:.3f} s")
    print(f"Impact Range          : {ballistic_path[-1, 0]:.2f} m")
    print(f"Impact Speed          : {np.linalg.norm(ballistic_path[-1, 2:]):.2f} m/s\n")
    print("==================================================")

if __name__ == "__main__":
    main()