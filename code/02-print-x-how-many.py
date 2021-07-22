#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:37:13 2021
How many times to print the letter X?
Use while loop. Move print under while block because it results in printing
each iteration.
@author: philip
"""
num_x = int(input('How many times should I print the letter X? '))
to_print = ''
counter = 0

while num_x > 0:
    to_print = num_x * 'X'
    num_x = num_x - 1
    print(to_print)
