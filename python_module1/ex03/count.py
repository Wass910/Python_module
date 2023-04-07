import sys
import string

def text_analyzer(s):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    res = isinstance(s, str)
    if res == False:
        print("AssertionError: argument is not a string")
        return

    nb_char = 0
    nb_upper = 0
    nb_lower = 0
    nb_ponc = 0
    nb_space = 0

    for a in s:
        if a == ' ':
            nb_space+=1
        elif a in string.punctuation:
            nb_ponc+=1
        elif (a >= "A" and a <= "Z"):
            nb_upper+=1
        elif (a >= "a" and a <= "z"):
            nb_lower+=1
        
    print("The text contains" , len(s) , "character(s):")
    print("-" , nb_upper , "upper letter(s)")
    print("-" , nb_lower , "lower letter(s)")
    print("-", nb_ponc, "punctuation mark(s)")
    print("-" , nb_space , "space(s)")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit()

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
        exit()

    text_analyzer(sys.argv[1])