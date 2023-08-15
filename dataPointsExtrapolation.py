import numpy as np

# Given data points
data = {
    1: 0.4,
    2: 1.4,
    3: 0.8,
    4: 0.6
}

# Calculate delta(x) (assuming constant)
delta_x = 1

# Calculate forward differences
first_forward_diff = data[2] - data[1]
second_forward_diff = data[3] - 2 * data[2] + data[1]
third_forward_diff = data[4] - 3 * data[3] + 3 * data[2] - data[1]

# Calculate the 5th data point using extrapolation
f_5th_data_point = data[4] + (1 / 4) * first_forward_diff + (1 / 8) * second_forward_diff + (1 / 48) * third_forward_diff

# Print the result
print("Estimated 5th Data Point using Extrapolation:", f_5th_data_point)
