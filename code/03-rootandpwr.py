#!/usr/bin/env python
# Ask user for an integer and print two integers: root and pwr
# such that 1 < pwr < 6 and root**pwr equals provided integer. If
# no such integers exist, it should print message to that effect.
# This solution came from Stackanovist on StackOverflow on 7 June 2020.
# https://stackoverflow.com/a/62243928. I like this one because it
# shows the process being used.
x = int(input('Enter an integer: '))
root = 0
pwr = 1
while pwr < 6:
    while root**pwr < abs(x):
        root += 1
    if abs(root**pwr) != abs(x):
        print('no root at the power', pwr, 'for', x)
    else:
        if x < 0:
            root = -root
            if pwr%2 != 0:
                print(root, "**", pwr, '=', x)
            else:
                print('no root at the power', pwr, 'for', x)
        else:
            print(root, "**", pwr, '=', x)
    root = 0
    pwr += 1
