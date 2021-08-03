#!/usr/bin/env python
# How many times to print the letter X?
# Use while loop. Move print under while block because it results in printing
# each iteration.
num_x = int(input('How many times should I print the letter X? '))
to_print = ''
counter = 0

while num_x > 0:
    to_print = num_x * 'X'
    num_x = num_x - 1
    print(to_print)

