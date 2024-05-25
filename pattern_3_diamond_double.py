from math import ceil

size_of_diamond = int(input())

upper_half_counter = ceil(size_of_diamond / 2) - 1
for row in range(1, size_of_diamond + 1, 2):
    print(upper_half_counter * ' ' + '*' * row)
    upper_half_counter -= 1

lower_half_counter = 0
for row in range(size_of_diamond - 1, 0, -2):
    print(lower_half_counter * ' ' + '*' * row)
    lower_half_counter += 1