import sys
if len(sys.argv)==2 :

    string=sys.argv[1]
    print(string[0])
    bool=True
    for char in string:
        if ord(char)>=48 and ord(char)<=57:
            bool=False
    if bool==True:
        compteur=0
        for char in string:
            compteur+=1
        print(compteur)
    else:
        print("erreur")
else:
    print("erreur")
#questionnement sur le type string. quand on donne des chiffres en entrée cela
#ne doit pas fonctionner/.
#table ascii , ord ?
#autre idée: vérifier que l'argument commence par " ou ' et finit par "ou '
#plus classe je pense .
