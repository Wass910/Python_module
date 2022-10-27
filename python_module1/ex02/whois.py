import sys

if len(sys.argv) == 1:
    exit()

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
    exit()

if sys.argv[1][0] == "-":
    sys.argv[1] = sys.argv[1][1:]

if sys.argv[1][0] == "+":
    sys.argv[1] = sys.argv[1][1:]

for a in sys.argv[1]:
    if (a < "0" or a > "9"):
        print("AssertionError: argument is not an integer")
        exit()

s = int(sys.argv[1])

if s == 0:
    print("I'm Zero.")
elif s % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")