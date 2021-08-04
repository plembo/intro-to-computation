#!/usr/bin/env python
# Bisection search algorithm for finding square root using high and low
# values
x = float(input('Enter a number: '))
epsilon = 0.01
num_guesses, low = 0,0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)
