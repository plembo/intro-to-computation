#!/usr/bin/env python
# Test if an int > 2 is prime. If not, print smallest divisor.
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
largest_divisor = None
for guess in range(2, x):
    if x%guess == 0:
        smallest_divisor = guess
        largest_divisor = x/guess
        largest_divisor = int(largest_divisor)
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
    print('Largest divisor of', x, 'is', largest_divisor)
else:
    print(x, 'is a prime number')
