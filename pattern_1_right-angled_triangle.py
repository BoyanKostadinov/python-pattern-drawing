# Pattern 1: Right-angled Triangle

number_symbols_last_row = int(input())
symbol = '*'

for index in range(1, number_symbols_last_row + 1):
    print(symbol * index)