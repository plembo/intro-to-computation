# Empire State building has 102 stories. Need to test for highest floor from
# which egg can be dropped without breaking. Limit of 7 eggs to work with.
# Find minimum trials for worst case
# k = floors
# n = eggs
# Solution from ita_c. "Egg Dropping Puzzle". _Geeks for Geeks_, 15 June 2021,
# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/. "Method 1:
# Recursion". Uses sys.max function.  This method takes a _long_ time once you
# ramp up to 102 floors, even on a pretty powerful machine. In fact, starts to
# stall at 16 floors and becomes completely unresponsive at 20.
import sys
 
# Function to get minimum number of trials
# needed in worst case with n eggs and k floors
def eggDrop(n, k):
 
    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (k == 1 or k == 0):
        return k
 
    # We need k trials for one egg
    # and k floors
    if (n == 1):
        return k
 
    min = sys.maxsize
 
    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):
 
        res = max(eggDrop(n - 1, x - 1),
                  eggDrop(n, k - x))
        if (res < min):
            min = res
 
    return min + 1
 
# Driver Code
if __name__ == "__main__":
 
    n = 7
    k = 19
    print("Minimum number of trials in worst case with",
           n, "eggs and", k, "floors is", eggDrop(n, k))
 
# This code is contributed by ita_c
