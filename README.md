# Flight Dynamics & Interception Simulation Engine

A modular Python library for numerical entry trajectories, multi-stage thrust integration, relative target navigation, and pursuit interception mechanics.

## Overview
This repository provides numerical simulation tools for aerospace flight mechanics and state vector analysis. Built modularly, the engine models atmospheric entry paths, dynamic thrust degradation under atmospheric drag, relative close-approach kinematics, and pursuit-evasion intercept metrics.

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