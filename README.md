# Flight Dynamics Engine in Python Code

This repository contains python source code for a modular Python library that calculates entry & reentry trajectories, multi-stage thrust integration, relative navigation, and flight interception.

## Key Features
* **Propulsion & Dynamic Drag:** Numerical integration of velocity under dynamic thrust profiles ($F_{\text{thrust}}(t) = 3000 - 100t$) and linear aerodynamic drag ($F_{\text{drag}} = -bv$).
* **Multi-Stage Thrust Profiles:** Piecewise state history calculation across burn, coast, and deceleration stages.
* **Guidance & Pursuit Interception:** Analytic quadratic pursuit solver for time-to-intercept, intercept range, and terminal velocity.
* **Planar Atmospheric Entry:** Numerical integration of ballistic flight trajectories over ground terrain under acceleration due to gravity.
* **Relative Kinematics:** Closest Point of Approach (CPA) vector calculation for two independent vehicles on intersecting vector paths.

## Repository Structure
```text
flight-dynamics-engine/
│
├── core/
│   ├── kinematics.py      # Polynomial kinematics & relative CPA vector dynamics
│   ├── propulsion.py      # Dynamic thrust/drag integration & multi-stage burn solvers
│   └── interception.py    # Pursuit guidance algorithms & ballistic entry integration
│
├── main.py                # Primary execution script for full simulation suite
└── README.md              # Project documentation
