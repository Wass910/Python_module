import sys
import string

if __name__ != "__main__":
    sys.exit()

if len(sys.argv) != 3:
    print("ERROR")
    quit()

try:
    lengh = int(sys.argv[2])
except:
    print("ERROR")
    quit()

all_word = sys.argv[1]
all_word = all_word.translate(str.maketrans('', '', string.punctuation))
all_word = all_word.split()
new_list = []

for word in all_word:
    if len(word) > lengh:
        new_list.append(word)
print(new_list)
