import sys
import string

if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>\nExample:\n      python operations.py 10 3")
    exit()

if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    exit()

for a in sys.argv[1]:
    if (a < "0" or a > "9"):
        print("AssertionError: argument is not an integer")
        exit()
    
for a in sys.argv[2]:
    if (a < "0" or a > "9"):
        print("AssertionError: argument is not an integer")
        exit()

value1 = int(sys.argv[1])
value2 = int(sys.argv[2])

print("Sum:       ", value1 + value2)
print("Difference:", value1 - value2)
print("Product:   ", value1 * value2)
try:
    print("Quotient:  ", value1 / value2)
    print("Remainder: ", value1 % value2)
except ZeroDivisionError:
    print("Quotient:   ERROR (division by zero)\nRemainder:  ERROR (modulo by zero)")
