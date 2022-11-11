import sys
import string

if __name__ != "__main__":
    sys.exit()
    
kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_0{kata[0]}, ex_0{kata[1]} : %.2f, {kata[3]:.2e}, {kata[4]:.2e}" % (kata[2]))