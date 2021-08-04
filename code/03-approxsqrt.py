#!/usr/bin/env python
# Guess square root of a number
x = float(input('Enter a number: '))
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    num_guesses += 1
print('number of guesses =', num_guesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on the square root of', x)
else:
    print(ans, 'is close to the square root of', x)
