import csv

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
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                indexes.append((row[0], row[1]))  # Store i7 and i5 as a tuple
    return indexes

def write_indexes_with_details_to_csv(indexes, output_file_path, collision_status, min_distances, closest_indexes, second_closest_indexes):
    """Write indexes and their details to a new CSV file."""
    with open(output_file_path, mode='w') as outfile:
        writer = csv.writer(outfile)
        # Write the header
        writer.writerow(["i7", "i5", "Collision", "Min Distance", "Closest Index", "Second Closest Index"])
        # Write the data with details
        for row, collision, min_dist, closest, second_closest in zip(indexes, collision_status, min_distances, closest_indexes, second_closest_indexes):
            writer.writerow([row[0], row[1], collision, min_dist, ''.join(closest), ''.join(second_closest)])

# Example usage:
input_file_path = 'indexes.csv'  # Replace with your actual input CSV file path
output_file_path = 'indexes_with_details.csv'  # Replace with your desired output CSV file path

# Read indexes from the input CSV file
indexes = read_indexes_from_csv(input_file_path)

# Combine i7 and i5 sequences into a single sequence for comparison
combined_indexes = [i7 + i5 for i7, i5 in indexes]

# Check for collisions
collision_status = [False] * len(combined_indexes)
for i in range(len(combined_indexes)):
    for j in range(i + 1, len(combined_indexes)):
        if hamming_distance(combined_indexes[i], combined_indexes[j]) < 3:
            collision_status[i] = True
            collision_status[j] = True

# Get minimum distances and closest indexes
min_distances, closest_indexes, second_closest_indexes = get_min_distances(combined_indexes)

# Write the results to the output CSV file (now pass `indexes` directly)
write_indexes_with_details_to_csv(indexes, output_file_path, collision_status, min_distances, closest_indexes, second_closest_indexes)

