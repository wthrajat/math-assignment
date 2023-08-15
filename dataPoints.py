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

# Calculate f'(x0) using backward-difference method (1st order)
f_prime_1st_order = (data[4] - data[3]) / delta_x

# Calculate f''(x0) using backward-difference method (2nd order)
f_double_prime_2nd_order = (data[4] - 2 * data[3] + data[2]) / (delta_x ** 2)

# Calculate f'''(x0) using backward-difference method (3rd order)
f_triple_prime_3rd_order = (data[4] - 3 * data[3] + 3 * data[2] - data[1]) / (delta_x ** 3)

# 0th order approximation (constant)
f_next_0th_order = data[4]

# 1st order approximation
f_next_1st_order = data[4] + f_prime_1st_order * delta_x

# 2nd order approximation
f_next_2nd_order = data[4] + f_prime_1st_order * delta_x + 0.5 * f_double_prime_2nd_order * (delta_x ** 2)

# 3rd order approximation
f_next_3rd_order = data[4] + f_prime_1st_order * delta_x + 0.5 * f_double_prime_2nd_order * (delta_x ** 2) + (1 / 6) * f_triple_prime_3rd_order * (delta_x ** 3)

# Print the results
print("0th Order Approximation:", f_next_0th_order)
print("1st Order Approximation:", f_next_1st_order)
print("2nd Order Approximation:", f_next_2nd_order)
print("3rd Order Approximation:", f_next_3rd_order)
