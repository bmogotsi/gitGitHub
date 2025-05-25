#! Python3
import sys 

# Using print() with * operator
# We can use print(*list_name) when we want a simple and clean display of list elements without additional formatting like brackets or commas.
# The * operator unpacks the list so that each element is printed individually.


a = [1, 2, 3, 4, 5]

# Print without using any separators
# between elements
print(*a)

# Print using separator (,)
print(*a, sep =', ')

# Print using separator (,)
print(*a, sep ='\p')