import re

# Read the input from the file
with open("day3.txt", "r") as file:
    data = file.read()

# Regular expression to match valid mul(X,Y) instructions
pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"

# Find all matches of the pattern in the input data
matches = re.findall(pattern, data)

# Calculate the sum of products
result_sum = sum(int(x) * int(y) for x, y in matches)

# Output the result
print(f"The sum of all valid multiplications is: {result_sum}")