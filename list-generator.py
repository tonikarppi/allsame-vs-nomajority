from random import randint, random, shuffle
from math import floor


def generate_no_majority_list(length):
    output = []
    i = 1
    while len(output) < length:
        max_times = floor(length/2) - i
        if max_times < 1:
            max_times = 1
        times = randint(1, max_times)
        num_list = [i] * times
        output.extend(num_list)
        i = i + 1
    return output[:length]


rand_list = generate_no_majority_list(1000000)
list_str = ' '.join(str(i) for i in rand_list)
print(list_str)
