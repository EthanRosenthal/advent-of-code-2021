with open("input.txt", "r") as f:
    lines = [int(line.strip("\n")) for line in f.readlines()]

num_increases = 0
for l1, l2 in zip(lines[:-1], lines[1:]):
    if l2 > l1:
        num_increases += 1

print("Part 1:")
print(f"Number of increases: {num_increases}")


num_increases = 0
for start_1, start_2 in zip(range(0, len(lines) - 3), range(1, len(lines) - 2)):
    sum_1 = sum(lines[start_1 : start_1 + 3])
    sum_2 = sum(lines[start_2 : start_2 + 3])

    if sum_2 > sum_1:
        num_increases += 1

print("Part 2:")
print(f"Number of increases: {num_increases}")
