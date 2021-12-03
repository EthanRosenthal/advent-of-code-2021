with open("input.txt", "r") as f:
    commands = [line.rstrip("\n").strip() for line in f.readlines()]

depth = 0
horizontal = 0

for command in commands:
    direction, amount = command.split()
    amount = int(amount)
    if direction == "up":
        depth -= amount
    elif direction == "down":
        depth += amount
    elif direction == "forward":
        horizontal += amount
    else:
        raise ValueError(f"Unknown direction {direction!r}")

print("Part 1:")
print(f"Depth={depth}, Horizontal={horizontal}, X = {depth * horizontal}")


depth = 0
horizontal = 0
aim = 0

for command in commands:
    direction, amount = command.split()
    amount = int(amount)
    if direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount
    elif direction == "forward":
        horizontal += amount
        depth += aim * amount
    else:
        raise ValueError(f"Unknown direction {direction!r}")

print("Part 2:")
print(f"Depth={depth}, Horizontal={horizontal}, X = {depth * horizontal}")
