with open("input.txt", "r") as f:
    numbers = [list(line.rstrip("\n").strip()) for line in f.readlines()]

gamma = []
epsilon = []
for bits in zip(*numbers):
    this_gamma = round(sum(int(x) for x in bits) / len(bits))
    # Flip from 1->0 or 0->1
    this_epsilon = 1 - this_gamma
    gamma.append(this_gamma)
    epsilon.append(this_epsilon)

gamma = int("".join(str(x) for x in gamma), 2)
epsilon = int("".join(str(x) for x in epsilon), 2)
print("Part 1:")
print(f"Gamma={gamma}, Epsilon={epsilon}, Gamma X Epsilon={gamma * epsilon}")

o2_index = None
co2_index = None
o2_indices = list(range(len(numbers)))
co2_indices = list(range(len(numbers)))
for bits in zip(*numbers):
    if o2_index is None:
        # Simple way to round up at 0.5 -> int(x + 0.5)
        o2_bits = [bits[i] for i in o2_indices]
        most_common_o2_value = int(sum(int(x) for x in o2_bits) / len(o2_bits) + 0.5)

        o2_indices = [
            idx
            for idx, value in enumerate(bits)
            if idx in o2_indices and int(value) == most_common_o2_value
        ]

        if len(o2_indices) == 1:
            # we're done
            o2_index = o2_indices[0]

    if co2_index is None:
        co2_bits = [bits[i] for i in co2_indices]
        most_common_co2_value = int(sum(int(x) for x in co2_bits) / len(co2_bits) + 0.5)
        least_common_co2_value = 1 - most_common_co2_value

        co2_indices = [
            idx
            for idx, value in enumerate(bits)
            if idx in co2_indices and int(value) == least_common_co2_value
        ]

        if len(co2_indices) == 1:
            # we're done
            co2_index = co2_indices[0]
    if o2_index is not None and co2_index is not None:
        break


if o2_index is None:
    raise ValueError(f"Unable to find oxygen level")
if co2_index is None:
    print(co2_indices)
    raise ValueError(f"Unable to find CO2 level")
o2 = int("".join(numbers[o2_index]), 2)
co2 = int("".join(numbers[co2_index]), 2)

print("Part 2:")
print(f"Oxygen level={o2}, CO2 level={co2}, O2 X CO2={o2 * co2}")
