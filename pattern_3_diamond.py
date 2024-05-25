# Pattern 3: Diamond

from math import ceil

size_of_diamond = int(input())

if size_of_diamond % 2 == 0:
    beginning_of_interval = 1
    counter_initial_value = 0
else:
    beginning_of_interval = 2
    counter_initial_value = 1

upper_half_counter = ceil(size_of_diamond / 2) - 1
for row in range(1, size_of_diamond + 1, 2):
    print(upper_half_counter * ' ' + '*' * row)
    upper_half_counter -= 1

lower_half_counter = counter_initial_value
for row in range(size_of_diamond - beginning_of_interval, 0, -2):
    print(lower_half_counter * ' ' + '*' * row)
    lower_half_counter += 1


# Alternative solution

from math import ceil
# size_of_diamond = int(input())

# # when the size of rhombus is an odd number
# upper_half_counter = ceil(size_of_diamond / 2) - 1
# for row in range(1, size_of_diamond + 1, 2):
#     print(upper_half_counter * ' ' + '*' * row)
#     upper_half_counter -= 1
#
# lower_half_counter = 1
# for row in range(size_of_diamond - 2, 0, -2):
#     print(lower_half_counter * ' ' + '*' * row)
#     lower_half_counter += 1


# # when the size of rhombus is an even number
# upper_half_counter = int(size_of_diamond / 2) - 1
# for row in range(1, size_of_diamond + 1, 2):
#     print(upper_half_counter * ' ' + '*' * row)
#     upper_half_counter -= 1
#
# lower_half_counter = 0
# for row in range(size_of_diamond - 1, 0, -2):
#     print(lower_half_counter * ' ' + '*' * row)
#     lower_half_counter += 1
