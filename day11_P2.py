import sys

def transform_stones(stones):
    """
    Perform one transformation ("blink") on the stones according to the rules.
    """
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)  # 0 becomes 1
        elif len(str(stone)) % 2 == 0:
            # Even-length stone splits into two stones
            dstr = str(stone)
            left = int(dstr[:len(dstr) // 2])
            right = int(dstr[len(dstr) // 2:])
            new_stones.extend([left, right])
        else:
            # Odd-length stone is replaced by the stone's value multiplied by 2024
            new_stones.append(stone * 2024)
    return new_stones

# Input data
initial_stones = [41078, 18, 7, 0, 4785508, 535256, 8154, 447]

# Number of blinks to simulate
num_blinks = 75

# Perform the transformations
stones = initial_stones
for _ in range(num_blinks):
    stones = transform_stones(stones)

# Output the number of stones after the specified blinks
print(f"Number of stones after {num_blinks} blinks: {len(stones)}")
