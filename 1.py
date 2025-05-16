def calculate_total_distance_from_file(filename):
    left_list = []
    right_list = []
    
    # Read the input file and populate the lists
    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Sort the lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance

# Replace 'input.txt' with the name of your input file
filename = 'paste.txt'
total_distance = calculate_total_distance_from_file(filename)
print(f"Total distance between the lists: {total_distance}")