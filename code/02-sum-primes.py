#!/usr/bin/env python
# Sum of primes more than 2 but less than 1000
# Counted number of primes found to validate operation
start = 2
finish = 1000

total = 0
count = 0

for num in range(start, finish):
    if num > start < finish:
        prime = True
        for i in range(2, num):
            if(num % i == 0):
                prime = False
        if prime:
            count += 1
            total += num

print(f'Number of primes between {start} and {finish} is {count}')
print(f'Sum of those primes is {total}')
Created on Thu Jul 22 12:40:53 2021
