# Pattern 5: Hollow Square

size_of_square = int(input())
symbol = '*'

print(symbol * size_of_square)

for index in range(size_of_square - 2):
    print(symbol + (size_of_square - 2) * ' ' + symbol)

print(symbol * size_of_square)