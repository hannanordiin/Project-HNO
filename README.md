Hamming Distance Index Collision Checker

import csv
import sys

def hamming_distance(seq1, seq2):
    """Calculate the Hamming distance between two sequences."""
    return sum(el1 != el2 for el1, el2 in zip(seq1, seq2))

def get_min_distances(indexes):
    """Get the minimum Hamming distances and the closest indexes for each index."""
    n = len(indexes)
    min_distances = [float('inf')] * n
    closest_indexes = [("", "")] * n
    second_closest_indexes = [("", "")] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = hamming_distance(indexes[i], indexes[j])
                if dist < min_distances[i]:
                    second_closest_indexes[i] = closest_indexes[i]
                    closest_indexes[i] = indexes[j]
                    min_distances[i] = dist
                elif dist < hamming_distance(indexes[i], second_closest_indexes[i]):
                    second_closest_indexes[i] = indexes[j]
    return min_distances, closest_indexes, second_closest_indexes

def read_indexes_from_csv(file_path):
    """Read indexes from a CSV file. Assumes the file has two columns without headers."""
    indexes = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print("Row:", row)  # Debug print to see each row
                if len(row) == 2:  # Check that each row has two columns
                    indexes.append((row[0], row[1]))  # Store i7 and i5 as a tuple
    except Exception as e:
        print("Error reading file:", e)  # Print any error that occurs
    return indexes

def write_indexes_with_details_to_csv(indexes, output_file_path, collision_status, min_distances, closest_indexes, second_closest_indexes):
    """Write indexes and their details to a new CSV file."""
    with open(output_file_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the header
        writer.writerow(["i7", "i5", "Collision", "Min Distance", "Closest Index", "Second Closest Index"])
        # Write the data with details
        for row, collision, min_dist, closest, second_closest in zip(indexes, collision_status, min_distances, closest_indexes, second_closest_indexes):
            writer.writerow([row[0], row[1], collision, min_dist, ''.join(closest), ''.join(second_closest)])

# Example usage with user input for file paths:
if len(sys.argv) < 3:
    print("Usage: python script.py <input_file_path> <output_file_path>")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Read indexes from the input CSV file
indexes = read_indexes_from_csv(input_file_path)

if not indexes:
    print("No indexes found in the input file.")
    sys.exit(1)

# Combine i7 and i5 sequences into a single sequence for comparison
combined_indexes = [i7 + i5 for i7, i5 in indexes]
print("Combined Indexes:", combined_indexes)  # Debug print to check combined indexes

# Check for collisions
collision_status = [False] * len(combined_indexes)
for i in range(len(combined_indexes)):
    for j in range(i + 1, len(combined_indexes)):
        if hamming_distance(combined_indexes[i], combined_indexes[j]) < 3:
            collision_status[i] = True
            collision_status[j] = True
print("Collision Status:", collision_status)  # Debug print to check collisions

# Get minimum distances and closest indexes
min_distances, closest_indexes, second_closest_indexes = get_min_distances(combined_indexes)
print("Min Distances:", min_distances)  # Debug print to check distances
print("Closest Indexes:", closest_indexes)  # Debug print to check closest indexes
print("Second Closest Indexes:", second_closest_indexes)  # Debug print to check second closest indexes

# Write the results to the output CSV file
write_indexes_with_details_to_csv(indexes, output_file_path, collision_status, min_distances, closest_indexes, second_closest_indexes)

print(f"Results written to {output_file_path}")
