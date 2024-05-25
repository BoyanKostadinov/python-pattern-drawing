# Pattern 6: Pyramid

number_of_rows = int(input())

upper_half_counter = number_of_rows - 1
for row in range(1, 2 * number_of_rows, 2):
    print(upper_half_counter * ' ' + '*' * row)
    upper_half_counter -= 1