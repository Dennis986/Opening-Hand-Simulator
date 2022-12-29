import random
import time

# Set the quota for the number of nonLand and Land cards
nonLand_quota = 33
Land_quota = 27

# Initialize a dictionary to store the frequency of the number of nonLands in each string
nonLand_frequency = {}

# Record the start time
start_time = time.time()

# Set the total number of binary strings to generate
total_strings = 1000000

# Generate binary strings
for i in range(total_strings):
  # Reset the quotas for each new string
  nonLand_quota = 33
  Land_quota = 27

  # Initialize the binary string
  binary_string = ""

  # Initialize the counter for the number of nonLands in the string
  num_nonLands = 0

  # Generate a 7-digit binary string
  for j in range(7):
    # Choose a random digit (either 1 or 0)
    digit = random.randint(0, 1)

    # If the digit quota for the chosen digit is not exhausted,
    # add the digit to the binary string and decrement the quota
    if digit == 1 and nonLand_quota > 0:
      binary_string += str(digit)
      nonLand_quota -= 1
      num_nonLands += 1
    elif digit == 0 and Land_quota > 0:
      binary_string += str(digit)
      Land_quota -= 1
    # If the digit quota for the chosen digit is exhausted,
    # choose the other digit and decrement its quota instead
    elif digit == 1 and nonLand_quota == 0:
      binary_string += "0"
      Land_quota -= 1
    elif digit == 0 and Land_quota == 0:
      binary_string += "1"
      num_nonLands += 1
      one_quota -= 1

  # Increment the frequency of the number of nonLands in the string
  if num_nonLands in nonLand_frequency:
    nonLand_frequency[num_nonLands] += 1
  else:
    nonLand_frequency[num_nonLands] = 1

  # Estimate and print the time left to complete the process
  if (i+1) % 10 == 0:
    time_elapsed = time.time() - start_time
    time_left = (time_elapsed / (i+1)) * (total_strings - (i+1))
    print(f"Time left: {time_left:.1f} seconds")

# Print the frequency of the number of ones in each string
for num_nonLands, frequency in nonLand_frequency.items():
  print(f"Number of strings with {num_nonLands} non_Land Cards: {frequency}")
