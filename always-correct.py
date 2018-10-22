from math import floor
from sys import stdin


# Determines if numbers in given list are all the same,
# or that there are no numbers that appear more than n/2 times.
# A: A list of numbers, lists with majority result in undefined behavior.
# Returns True if all numbers are the same, or False if no-majority.
def all_same_or_no_majority(A):
    n = len(A)
    for i in range(1, floor(n/2)+1):
        if A[i] != A[0]:
            return False
    return True


num_list_str = stdin.readline()
num_list = [int(s) for s in num_list_str.split(' ')]
result = all_same_or_no_majority(num_list)
print(result)
