# Compare bisection to Newton methods of finding
# square root
print('Find the square root of a number')
k = float(input('Enter a number: '))
epsilon = 0.01

print('First, try a bisection search')
num_guesses, low = 0,0
high = max(1, k)
ans = (high + low)/2

while abs(ans**2 - k) >= epsilon:
    num_guesses += 1
    if ans**2 < k:
        low = ans
    else:
        high = ans
    ans = (high + low)/2


print(ans, 'is close to the sqrt of', k)
print('Number of guesses =', num_guesses)

print('-------------------------------------')
print('Next, try Newton-Raphson')

guess = k / 2
count = 0

while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
    count += 1

print(guess, 'is close to sqrt of', k)
print('Number of guesses =', count)
print('')
print('Looks like Newton always wins!')
