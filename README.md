# Hamming Distance Index Collision Checker

## Overview
This Python script is designed to calculate the Hamming distance between pairs of combined i7 and i5 indexes from a CSV file. It identifies potential "collisions" between indexes and generates an output CSV file containing the indexes, their collision status, the minimum Hamming distances, and their closest/second-closest matches.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [How to Use](#how-to-use)
   - [Command-Line Arguments](#command-line-arguments)
   - [Example Usage](#example-usage)
3. [Script Breakdown](#script-breakdown)
   - [Reading Input](#reading-input)
   - [Calculating Hamming Distance](#calculating-hamming-distance)
   - [Checking Collisions](#checking-collisions)
   - [Writing Output](#writing-output)
4. [File Formats](#file-formats)
5. [Troubleshooting](#troubleshooting)

## Prerequisites
* Python installed
* A CSV file containing two columns of i7 and i5 indexes.

## How to Use

### Command-Line Arguments
The script expects two arguments:

1. Input CSV File: The path to the CSV file containing i7 and i5 indexes.
2. Output CSV File: The path where the output with details will be saved.

### Example Usage
To run the script from the terminal:

`python script.py path/to/input.csv path/to/output.csv`

Example: 

`python script.py indexes.csv indexes_with_details.csv`

## Script Breakdown

### Reading Input
The script reads the input CSV file provided by the user. Each row in the file should contain two values: the i7 index and the i5 index. These indexes are combined into a single sequence for comparison.

Relevant code section: 

`indexes = read_indexes_from_csv(input_file_path)`


### Calculating Hamming Distance
The Hamming distance between pairs of combined indexes is calculated. The Hamming distance is the number of positions at which the corresponding symbols differ between two sequences.

Relevant code section: 
```
def hamming_distance(seq1, seq2):
    return sum(el1 != el2 for el1, el2 in zip(seq1, seq2))`
```


### Checking Collisions
The script checks for collisions, defined as any two indexes that have a Hamming distance less than 3. If such a collision is detected, it marks both indexes as "collided."

Relevant code section: 
```
if hamming_distance(combined_indexes[i], combined_indexes[j]) < 3:
    collision_status[i] = True
    collision_status[j] = True
```

### Writing Output
The results, including collision status, minimum distances, and closest matches, are written to a new CSV file. The output file will include:

* i7 and i5 indexes.
* Whether a collision was detected.
* The minimum Hamming distance.
* The closest and second closest index sequences.

Relevant code section: 

`write_indexes_with_details_to_csv(indexes, output_file_path, collision_status, min_distances, closest_indexes, second_closest_indexes)`

## File Formats

### Input CSV Format
The input CSV file should have two columns:

* i7 index (first column).
* i5 index (second column).

### Output CSV Format
The output file will contain the following columns:

* i7 index.
* i5 index.
* Collision Status (True/False).
* Minimum Hamming Distance.
* Closest Index.
* Second Closest Index.

## Troubleshooting
No Data in Output:

* Ensure your input file contains valid i7 and i5 sequences, with exactly two columns.
* Check the debug prints if enabled.

File Path Issues:

* Ensure that the file paths for input and output CSVs are correct and accessible.

Incorrect Format:

* Ensure your CSV file has the correct format: two columns without headers.

