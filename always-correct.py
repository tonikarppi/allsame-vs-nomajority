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

# A1 = [1, 1, 1, 1, 1]
# A2 = [1, 1, 1, 1]
# A3 = [1, 1, 2, 2]
# A4 = [1, 2, 3, 4]
# A5 = [1, 1, 5, 1, 3, 4]
# A6 = [1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 89, 1, 49, 1, 1, 1, 58, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 79, 1, 1, 1, 69, 74, 1, 87, 1, 1, 1]

# inputs = [A1, A2, A3, A4, A5, A6]

# for A in inputs:
#     result1 = all_same_or_no_majority(A)
#     print(result1)
