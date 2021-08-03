#!/usr/bin/env python
# Ask user to input 10 integers and then print largest odd number entered. If
# no odds entered, it should print message to that effect.
num_input = input('Enter 10 comma-separated integers, include some odd:')

num_list = num_input.split(',')
list_len = len(num_list)


if list_len != 10:
    print(f'You were asked for 10 integers, you provided {list_len}!')
else:
    # Test each number in the list and make a list of odds
    odd_list = []

    for i in num_list:
        if int(i) % 2 != 0:
            odd_list.append(i)
    # Make sure there's at least one odd number, if not warn user            
    if len(odd_list) < 1:
        print('You did not provide any odd numbers!') 
    else:
        # If there are odd numbers, find the largest and print
        largest_odd = max(odd_list)
        print(f'This was the largest odd number you provided: {largest_odd}')
