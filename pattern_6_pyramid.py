# Pattern 6: Pyramid

number_of_rows = int(input())

counter_blank_spaces = number_of_rows - 1
for row in range(1, 2 * number_of_rows, 2):
    print(counter_blank_spaces * ' ' + '*' * row)
    counter_blank_spaces -= 1