import random
import time

# Set the total number of strings to generate
total_strings = 100000

# Set the number of ones and zeros in each string
num_ones = 38
num_zeros = 22

# Set the start time
start_time = time.time()

# Initialize a dictionary to store the frequency of ones in each string
ones_frequency = {}

# Generate the strings
for i in range(total_strings):
    # Initialize the string with the required number of ones and zeros
    binary_string = ['1'] * num_ones + ['0'] * num_zeros

    # Shuffle the list to randomize the string
    random.shuffle(binary_string)

    # Convert the list to a string and count the number of ones in the first seven digits
    binary_string = ''.join(binary_string)
    num_ones_in_string = binary_string[:7].count('1')

    # Increment the frequency for the number of ones in the string
    if num_ones_in_string in ones_frequency:
        ones_frequency[num_ones_in_string] += 1
    else:
        ones_frequency[num_ones_in_string] = 1

    # Calculate the elapsed time and remaining time
    # Print the remaining time with a one-second delay and to 2 decimal places
    elapsed_time = time.time() - start_time
    remaining_time = (total_strings - i) * elapsed_time / (i+1)
    print(f"Estimated time left: {remaining_time:.1f} seconds")

# Print the frequency of ones in each string
print(ones_frequency)
