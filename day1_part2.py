from collections import Counter

def calculate_similarity_score(filename):
    left_list = []
    right_list = []
    
    # Read the input file and populate the lists
    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    
    return similarity_score

# Replace 'input.txt' with the name of your input file
filename = 'day1_p2.txt'
similarity_score = calculate_similarity_score(filename)
print(f"Similarity score: {similarity_score}")