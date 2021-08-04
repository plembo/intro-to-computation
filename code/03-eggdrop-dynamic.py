# Empire State building has 102 stories. Need to test for highest floor from
# which egg can be dropped without breaking. Limit of 7 eggs to work with.
# Find minimum trials for worst case
# k = floors
# n = eggs
# Solution from Bhavya Jain. "Egg Dropping Puzzle". _Geeks for Geeks_,
# 15 June 2021, https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/.
# "Method 2: Dynamic Programming". MUch quicker, but sadly tells us that
# you're going to use all your eggs!

INT_MAX = 32767
 
# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n, k):
    # A 2D table where entry eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]
 
    # We need one trial for one floor and0 trials for 0 floors
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
 
    # We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        eggFloor[1][j] = j
 
    # Fill rest of the entries in table using optimal substructure
    # property
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
 
    # eggFloor[n][k] holds the result
    return eggFloor[n][k]
 
# Driver program to test to pront printDups
n = 7
k = 102
print("Minimum number of trials in worst case with" + str(n) + "eggs and "
       + str(k) + " floors is " + str(eggDrop(n, k)))
 
# This code is contributed by Bhavya Jain
