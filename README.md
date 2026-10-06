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

## Python concepts used

- Classes and objects (`__init__`, `__str__`, `__repr__`, class attributes)
- Methods and helper functions (including a function outside the class)
- Lists, tuples, sets and dictionaries
- `for` and `while` loops, nested loops, `break`, `continue`, `return`
- `if` / `elif` / `else` conditions
- String methods (`upper()`, `isdigit()`) and f-strings
- Modulo (`%`) for turning left and right
- Error handling with `raise ValueError` and `try` / `except`
- The `random` module
- Default parameters and keyword arguments
- `if __name__ == "__main__":`
