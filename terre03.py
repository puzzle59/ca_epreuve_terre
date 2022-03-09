import sys
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lettre_curseur=sys.argv[1]
curseur=alphabet.index(lettre_curseur)
for i in range(curseur,len(alphabet)):
    print(alphabet[i],end="")
