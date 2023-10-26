import numpy as np
import matplotlib.pyplot as plt


def decimal_to_ternary(decimal, precision=10):
    result = "0."

    for _ in range(precision):
        decimal *= 3
        digit = int(decimal)
        result += str(digit)
        decimal -= digit

    return result


def binary_fraction_to_decimal(binary_fraction):
    decimal_fraction = 0.0
    for i, bit in enumerate(binary_fraction[2:]):
        decimal_fraction += int(bit) * (2 ** -(i + 1))
    return decimal_fraction


def cantorFunction(n):
    your_string = decimal_to_ternary(n)
    
    first_one_index = your_string.find("1")  # Find the index of the first "1"
    if first_one_index != -1:  # Check if "1" is found
        modified_string = your_string[:first_one_index + 1] + "0" * (len(your_string) - first_one_index - 1)
    else:
        modified_string = your_string

    modified_string = modified_string.replace("2", "1")
    return float(binary_fraction_to_decimal(modified_string))

limit = 1000001
x = []
y = []
for i in range(0, limit):
    n = i / (limit - 1)
    c = cantorFunction(n)
    x.append(n)
    y.append(c)

fig, ax = plt.subplots()

print(x)
print(y)
ax.scatter(x, y)

plt.show()