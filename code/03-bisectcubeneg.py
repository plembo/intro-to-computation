#!/usr/bin/env python
# Bisection search algorithm for finding cube root using high and low
# values. Allow for negative numbers.
x = float(input('Enter a number: '))
epsilon = 0.01
num_guesses, low = 0,0
high = max(1, x)

# Test for negative number and make low = x instead of 0
if x < 0:
    low = x
else:
    None
    
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
print(ans, 'is close to cube root of', x)
