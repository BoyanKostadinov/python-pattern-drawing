# Pattern 4: Left-angled Triangle

number_symbols_first_row = int(input())
symbol = '*'

for index in range(number_symbols_first_row, 0, -1):
    print(symbol * index)