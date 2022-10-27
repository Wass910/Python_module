import sys
import string

if __name__ != "__main__":
    sys.exit()
    
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for cle, valeur in kata.items():
    print (cle , " was created by", valeur)