def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power % 2 == 0:
        return None  # Negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans


approx_sqrt = find_root(25, 2, 0.001)
approx_cbrt = find_root(-8, 3, 0.001)
approx_4rt = find_root(16, 2, 0.001)

sum_root = approx_sqrt + approx_cbrt + approx_4rt

print("Sum of approximates: ", sum_root)
