# Robot Simulator

A small Python project: a robot that moves on a grid with obstacles.
Built while learning Python.

## Features

- Commands: `F` (forward), `B` (backward), `L` (turn left), `R` (turn right)
- Repeat counts, e.g. `3F` or `2R`
- Obstacles and wall collision
- Path tracking and ASCII map drawing
- Random obstacle generation
- Input validation (invalid direction or start position)
- `reset()` to return the robot to its start

## How to run

```
python robot.py
```

## Example

```python
obstacles = random_obstacles(5, 10, 10, (0, 0))
r = Robot(0, 0, "E", width=10, height=10, obstacles=obstacles)
r.run("5FRF")
r.draw()
```

Map symbols: `^ > v <` is the robot, `*` is its path, `#` is an obstacle, `.` is an empty cell.

## Ideas for the future

- Treasures and a goal flag
- Undo and command history
