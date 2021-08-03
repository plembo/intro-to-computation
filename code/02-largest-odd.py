#!/usr/bin/env python
# Print the larges odd number of x, y or z
x = 2
y = 3
z = 4

answer = min(x, y, z)
if x%2 != 0:
    answer = x
if y%2 != 0 and y > answer:
    answer = y
if z%2 != 0 and z > answer:
    answer = z
print(answer)
