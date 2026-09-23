# Flight Dynamics Engine in Python Code

This repository contains python source code for a modular Python library that calculates entry & reentry trajectories, multi-stage thrust integration, relative navigation, and flight interception.

core/ - kinematics.py (polynomial kinematics & CPA), propulsion.py (Multi-stage burn, thrust, and drag profiles), interception.py (ballistic integration)

Main.py - Executes the collection of python files to simulate flight dynamics

## Key Features

* **Propulsion & Drag:** Analyzes thrust conditions to determine the behavior of its velocity by applying numerical integration.
* **Multi-Stage Thrust:** This data is captured by utilizing piecewise functions to express each phase of the flight, connecting flight segments with their respected acceleration stages.
* **Guidance & Pursuit Interception:** Applies a quadratic pursuit solver to determine intercept time, range, and velocity impact.
* **Ballistic & Atmospheric Entry:** Applies numerical integration for ballistic reentry, calculating and modeling trajectories that are influenced by acceleration due to gravity.
* **Relative Kinematics:** Calculating Closest Point of Approach (CPA) for two vehicles that are independent of each other as vectors on a two dimensional plane.
