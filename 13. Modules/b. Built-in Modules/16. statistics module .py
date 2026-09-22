# A Program to calculate statistics using the statistics module

import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Mode:", statistics.mode([1, 2, 2, 3, 4]))
print("Standard deviation:", statistics.stdev(numbers))

# Explanation:
# The statistics module provides common statistical calculations.
# mean() calculates the average value.
# median() finds the middle value.
# mode() finds the most frequently occurring value.
# stdev() calculates standard deviation.

# Real-Life Use:
# Statistics are used in data analysis, research, performance reports, and machine learning preparation.