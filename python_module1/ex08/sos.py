import sys
import string

if __name__ != "__main__":
    sys.exit()

if len(sys.argv) == 1:
    print("ERROR")
    quit()

morse_dico = {
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/"
}

lengh = len(sys.argv) - 1
i = 2
to_translate = sys.argv[1]
translate = ""

while i <= lengh:
    to_translate = to_translate + " " + sys.argv[i]
    i = i+1

to_translate = to_translate.upper()
i = 0

while i < len(to_translate):
    if to_translate[i] in string.punctuation:
        print("ERROR")
        quit()
    if to_translate[i] == " ":
        translate = translate + "/ " 
    else:
        translate = translate + morse_dico.get(to_translate[i]) + " "
    i = i + 1

print(translate)
