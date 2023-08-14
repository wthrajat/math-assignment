import math

x = 0.13
E = 0.0001 # Error 0.01%

n = 0
term = (x ** (n + 1)) / math.factorial(n + 1)

while term > E:
    n += 1
    term = (x ** (n + 1)) / math.factorial(n + 1)

print("Number of terms required:", n)