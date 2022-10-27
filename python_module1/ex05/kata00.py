import sys
import string

if __name__ != "__main__":
    sys.exit()
    
kata = (19,42,21)
s = ''
for a in kata:
    s = s + a.__str__() + ', '

s = s[:-1]
s = s[:-1]
print ("The %d numbers are: %s" % (len(kata), s))