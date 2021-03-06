#!/usr/bin/env python
# Find primes between 2 and 1000
start = 2
finish = 1000

total = 0

for num in range(2, 1000):
    if num > start < finish:
        prime = True
        for i in range(2, num):
            if(num % i == 0):
                prime = False
        if prime:
            print(num)
            total += num

print(f'Sum of primes greater than {start} and less than {finish} is: {total}')
