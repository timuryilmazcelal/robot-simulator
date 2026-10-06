import random

def random_obstacles(count, width, height, start):
    max_obstacles = width * height - 1
    if count > max_obstacles:
        raise ValueError(f"Cannot place {count} obstacles in a {width}x{height} grid with start position {start}")
    obstacles = set()
    while len(obstacles) < count:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if (x, y) == start:
            continue
        obstacles.add((x, y))
    return list(obstacles)

class Robot:


    directions = ["N", "E", "S", "W"]
    moves = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

    def __init__(self, x, y, direction="N", width=10, height=10, obstacles=None):
        direction = direction.upper()
        if direction not in self.directions:
            raise ValueError("Invalid direction")
        self.width = width
        self.height = height
        self.obstacles = set(obstacles) if obstacles else set()
        if not self.is_free(x, y):
            raise ValueError("Initial position is blocked by an obstacle or out of bounds")
        self.x = x
        self.y = y
        self.direction = direction
        self.path = [(x, y)]
        self.start_x = x
        self.start_y = y
        self.start_direction = direction

    def __str__(self):
        return f"Robot({self.x}, {self.y}, {self.direction})"

    def __repr__(self):
        return f"Robot(x={self.x}, y={self.y}, direction={self.direction!r})"

    def move_forward(self):
        dx, dy = self.moves[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if self.is_free(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.path.append((new_x, new_y))
            return True
        else:
            print(f"Move blocked")
            return False

    def move_backward(self):
        dx, dy = self.moves[self.direction]
        new_x = self.x - dx
        new_y = self.y - dy
        if self.is_free(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.path.append((new_x, new_y))
            return True
        else:
            print(f"Move blocked")
            return False

    def turn_right(self):
        i = self.directions.index(self.direction)
        new_i = (i + 1) % len(self.directions)
        self.direction = self.directions[new_i]

    def turn_left(self):
        i = self.directions.index(self.direction)
        new_i = (i - 1) % len(self.directions)
        self.direction = self.directions[new_i]

    def is_free(self, x, y):
        return (x, y) not in self.obstacles and 0 <= x < self.width and 0 <= y < self.height

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.direction = self.start_direction
        self.path = [(self.start_x, self.start_y)]

    def run(self, commands):
        commands = commands.upper()
        count = 0
        number = ""
        for command in commands:
            if command.isdigit():
                number += command
                continue

            times = int(number) if number else 1
            number = ""

            if command not in "FBLR":
                print(f"Invalid command: {command}")
                continue

            for _ in range(times):
                if command == "F":
                    if not self.move_forward():
                        return count
                    count += 1

                elif command == "L":
                    self.turn_left()
                    count += 1

                elif command == "R":
                    self.turn_right()
                    count += 1

                elif command == "B":
                    if not self.move_backward():
                        return count
                    count += 1
        return count

    def draw(self):
        arrows = {"N": "^", "E": ">", "S": "v", "W": "<"}
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) in self.obstacles:
                    row += "#"
                elif (x, y) == (self.x, self.y):
                    row += arrows[self.direction]
                elif (x, y) in self.path:
                    row += "*"
                else:
                    row += "."
            print(row)

if __name__ == "__main__":
  
    print("--- Test 1: draw ---")
    r = Robot(1, 1, "E", width=5, height=4, obstacles=[(3, 1)])
    r.draw()

    print("--- Test 2: hit an obstacle ---")
    r = Robot(0, 0, "E", width=5, height=5, obstacles=[(3, 0)])
    r.run("FFF")
    r.draw()
    print(r)

    print("--- Test 3: hit a wall ---")
    r = Robot(0, 0, "N", width=5, height=5)
    r.run("LF")
    print(r)

    print("--- Test 4: invalid command ---")
    r = Robot(0, 0, "E")
    r.run("FXF")
    print(r)

    print("--- Test 5: lowercase direction ---")
    r = Robot(0, 0, "e")
    print(r)

    print("--- Test 6: invalid direction ---")
    try:
        r = Robot(0, 0, "X")
    except ValueError as e:
        print("Caught error:", e)

    print("--- Test 7: start on an obstacle ---")
    try:
        r = Robot(1, 1, "N", width=5, height=5, obstacles=[(1, 1)])
    except ValueError as e:
        print("Caught error:", e)

    print("--- Test 8: start outside the map ---")
    try:
        r = Robot(99, 99, "N", width=5, height=5)
    except ValueError as e:
        print("Caught error:", e)

    print("--- Test 9: initial path ---")
    r = Robot(2, 2, "E")
    print(r.path)

    print("--- Test 10: path after forward moves ---")
    r = Robot(2, 2, "E")
    r.run("FF")
    print(r.path)

    print("--- Test 11: path after backward move ---")
    r = Robot(2, 2, "E")
    r.run("FB")
    print(r.path)

    print("--- Test 12: draw with path ---")
    r = Robot(0, 0, "E", width=5, height=3)
    r.run("FFRF")
    r.draw()

    print("--- Test 13: start values are kept ---")
    r = Robot(2, 2, "E")
    r.run("FF")
    print(r)
    print(r.start_x, r.start_y, r.start_direction)

    print("--- Test 14: reset ---")
    r = Robot(2, 2, "E")
    r.run("FFRF")
    print(r)
    print(r.path)
    r.reset()
    print(r)
    print(r.path)

    print("--- Test 15: run returns count ---")
    r = Robot(0, 0, "E", width=5, height=5, obstacles=[(3, 0)])
    print(r.run("FFFF"))

    print("--- Test 16: repeat F ---")
    r = Robot(0, 0, "E", width=10, height=5)
    print(r.run("3F"))
    print(r)

    print("--- Test 17: repeat F blocked by obstacle ---")
    r = Robot(0, 0, "E", width=10, height=5, obstacles=[(2, 0)])
    print(r.run("5F"))
    print(r)

    print("--- Test 18: repeat turn ---")
    r = Robot(0, 0, "N")
    r.run("2R")
    print(r)

    print("--- Test 19: invalid command with repeat ---")
    r = Robot(0, 0, "E")
    print(r.run("3XF"))
    print(r)

    print("--- Test 20: one random obstacle ---")
    print(random_obstacles(1, 5, 5, (0, 0)))

    print("--- Test 21: five random obstacles ---")
    print(random_obstacles(5, 5, 5, (0, 0)))

    print("--- Test 22: start is never an obstacle ---")
    print(random_obstacles(3, 2, 2, (0, 0)))

    print("--- Test 23: too many obstacles ---")
    try:
        print(random_obstacles(5, 2, 2, (0, 0)))
    except ValueError as e:
        print("Caught error:", e)

    print("--- Test 24: random map ---")
    obstacles = random_obstacles(5, 10, 10, (0, 0))
    r = Robot(0, 0, "E", width=10, height=10, obstacles=obstacles)
    r.run("5FRF")
    r.draw()