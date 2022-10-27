import sys

if len(sys.argv) == 1:
    exit()

i = 1
s = ""

while i < len(sys.argv):
    s = s + sys.argv[i]
    s = s + " "
    i+=1   

s = s.rstrip(" ")
print(s[::-1].swapcase()) 