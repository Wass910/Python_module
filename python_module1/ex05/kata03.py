import sys
import string

if __name__ != "__main__":
    sys.exit()

kata = "The right format"
width = 42 - kata.__len__() - 1

print(f"{'-':->{width}}" + kata)