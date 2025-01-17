## Setup

- `Ubuntu 20.04` is recommended

- Install `Ego-Planner` following the instructions and make sure it is installed in your **home** directory `(e.g., /home/<your-username>/ego-planner)`: &emsp;<https://github.com/ZJU-FAST-Lab/ego-planner/tree/master>

- Execute the official example to ensure `Ego-Planner` is correctly installed.

- Clone the source code


## Replay 

- Execute `replay.py` to replay vulnerability type #1 scenario:
```javascript
python3 replay.py type1
```

- Open another new terminal and launch `rviz`:
```javascript
roslaunch ego_planner rviz.launch
```

- Open another new terminal and launch `Ego-Planner`:
```javascript
roslaunch ego_planner run_in_sim.launch
```

- Similarly, to replay other vulnerability types, execute:
```javascript
python3 replay.py folder_name
# for example:
python3 replay.py type2 (replay vulnerability type #2 scenario)
```

## Note
- As path planners use fast search algorithms (e.g. A*, RRT*) to randomly search for a path, the vulnerability may not trigger every time. 
If the vulnerability is not triggered, please **retry**.

- We simulated a 0.3 m wheelbase drone, thus a collision is assumed when the drone center reaches an obstacle distance within 0.15 m, equivalent to half the wheelbase length.