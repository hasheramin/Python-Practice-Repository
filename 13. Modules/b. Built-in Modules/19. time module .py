# A Program to measure execution time using the time module

import time

start_time = time.time()

total = 0

for number in range(1, 1000001):
    total += number

end_time = time.time()

execution_time = end_time - start_time

print("Total:", total)
print("Execution time:", execution_time, "seconds")

# Explanation:
# time.time() returns the current time as a timestamp.
# We store the timestamp before the operation.
# After the loop finishes, we take another timestamp.
# Subtracting both values gives an approximate execution time.

# Real-Life Use:
# Execution-time measurement is useful for performance testing, optimization, benchmarking, and comparing different solutions.