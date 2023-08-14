import math

def new_function(x, n):
    total = 0.0
    for i in range(n):
        term = ((1.43 * x + 0.53) ** (2 * i)) / (math.factorial(i + 3) * math.factorial(i + 1))
        total += term
    return total

def calculate_approximate_error(approximation, true_value):
    return abs(approximation - true_value) / true_value * 100

desired_error = 0.005 / 100  # Converting percentage to decimal

# Calculate true value using a larger number of terms (adjust as needed)
true_value = new_function(math.sqrt(3), 10)

n = 1
approximation = new_function(x, n)
error_estimate = calculate_approximate_error(approximation, true_value)

while error_estimate >= desired_error:
    n += 1
    approximation = new_function(x, n)
    error_estimate = calculate_approximate_error(approximation, true_value)

print("Number of terms required:", n)
print("Approximate value of New(x):", approximation)
print("True value of New(x):", true_value)
print("Approximate error estimate:", error_estimate, "%")
print("infinity", math.inf)