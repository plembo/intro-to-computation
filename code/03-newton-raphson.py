# Newton-Raphson for square root
# Find such that x**2 - 24 is within epsilon of 0
# k is the number
epsilon = 0.01
k = 100
guess = k / 2
count = 0

while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
    count += 1
print('Square root of', k, 'is about', guess)
print('Number of iterations required:', count)
