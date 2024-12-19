# Investigated drone path planners in detail

This page contains the drone path planners we investigated in detail, which is mentioned in IV. Evaluation A. Experiment setup.
We summarized the drone path planners as a below table. 

- Year: Published year.
- Title: The name of path planner or Github repository.
- Paper: If the path planner has published as a research paper, 'O' is marked.
- Code: If the code of path planner not available, 'X' is marked.
- Autonomous: If the path planner operates in uncharted environments, it is marked with 'O'. Some path planners rely on a global map and cannot autonomously search for paths. They are incapable of navigating obstacles and reaching destinations in cluttered and uncharted environments.
- Popularity: Star of the path planner if open source, 'X' else.
- Simulation: If the path planner support drone simulator, 'O' is marked. Some path planners only support numerical simulation, which are only for theory analysis, also marked as 'X'.
- Practicalness: If the path planner widely deployed on real world drones, 'O' is marked.

| ID | Year | Title                        | Paper                                                                                            | Code                                                             | Popularity | Autonomous | Simulation | Practicalness |
|----|------|------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------|------------|------------|---------------|
| A1 | 2020 | Ego Planner                  | EGO-Planner: An ESDF-free Gradient-based Local Planner for Quadrotors                            | [Link](https://github.com/ZJU-FAST-Lab/ego-planner/tree/master)  | 1.2k star  | O          | O          | O             |
| A2 | 2021 | Ego Planner Swarm            | EGO-Swarm: A Fully Autonomous and Decentralized Quadrotor Swarm System in Cluttered Environments | [Link](https://github.com/ZJU-FAST-Lab/ego-planner-swarm)        | 1.1k star  | O          | O          | O             |
| A3 | 2021 | FUEL                         | FUEL: Fast UAV Exploration using Incremental Frontier Structure and Hierarchical Planning        | [Link](https://github.com/HKUST-Aerial-Robotics/FUEL/tree/main)  | 885  star  | O          | O          | O             |
| 1  | 2016 | AvisionMissionPlanner        | X                                                                                                | [Link](https://github.com/AvisionRobotics/AvisionMissionPlanner) | 3 star     | X          | X          | X             |
| 2  | 2020 | mbplanner                    | Motion Primitives-based Agile Exploration Path Planning for Aerial Robotics                      | [Link](https://github.com/ntnu-arl/mbplanner_ros)                | 295 star   | O          | O          | X             |
| 3  | 2019 | Fast Planner[1]              | X                                                                                                | [Link](https://github.com/HKUST-Aerial-Robotics/Fast-Planner)    | 2.1k star  | O          | O          | X             |
| 4  | 2016 | path_planner[2]              | X                                                                                                | [Link](https://github.com/karlkurzer/path_planner)               | 1.4k star  | X          | X          | X             |
| 5  | 2020 | full_coverage_path_planner   | X                                                                                                | [Link](https://github.com/nobleo/full_coverage_path_planner)     | 501 star   | X          | X          | X             |
| 6  | 2020 | TopoTraj                     | Robust Real-time UAV Replanning Using Guided Gradient-based Optimization and Topological Paths   | [Link](https://github.com/HKUST-Aerial-Robotics/TopoTraj)        | 79 star    | O          | O          | X             |
| 7  | 2023 | ros_motion_planning[2]       | X                                                                                                | [Link](https://github.com/ai-winter/ros_motion_planning)         | 1.4k star  | X          | X          | X             |
| 8  | 2023 | matlab_motion_planning[2]    | X                                                                                                | [Link](https://github.com/ai-winter/matlab_motion_planning)      | 152 star   | X          | X          | X             |
| 9  | 2020 | PathPlanning[2]              | X                                                                                                | [Link](https://github.com/zhm-real/PathPlanning)                 | 7.2k star  | X          | X          | X             |
| 10 | 2019 | multi_agent_path_planning[2] | Nonlinear Model Predictive Control for Multi-Micro Aerial Vehicle Robust Collision Avoidance     | [Link](https://github.com/atb033/multi_agent_path_planning)      | 955 star   | X          | X          | X             |
| 11 | 2019 | faster                       | Fast and Safe Trajectory Planner for Flights in Unknown Environments                             | [Link](https://github.com/mit-acl/faster)                        | 848 star   | O          | X          | O             |
| 12 | 2019 | mav_active_3d_planning       | An Efficient Sampling-Based Method for Online Informative Path Planning in Unknown Environments  | [Link](https://github.com/ethz-asl/mav_active_3d_planning)       | 500 star   | O          | O          | X             |
| 13 | 2020 | mader[2]                     | MADER: Trajectory Planner in Multi-Agent and Dynamic Environments                                | [Link](https://github.com/mit-acl/mader)                         | 443 star   | O          | O          | X             |
| 14 | 2017 | path_planning                | X                                                                                                | [Link](https://github.com/ayushgaud/path_planning)               | 310 star   | O          | O          | X             |
| 15 | 2018 | OctomapPlanner               | X                                                                                                | [Link](https://github.com/ArduPilot/OctomapPlanner)              | 113 star   | O          | O          | X             |
| 16 | 2018 | motion_planning              | X                                                                                                | [Link](https://github.com/RuslanAgishev/motion_planning)         | 303 star   | X          | X          | X             |
| 17 | 2017 | RealTimePathPlanning         | X                                                                                                | [Link](https://github.com/rishabh1b/RealTimePathPlanning)        | 295 star   | X          | X          | X             |


[1] An early version of Ego Planner.

[2] Theory analysis for algorithms, not for real drone.
