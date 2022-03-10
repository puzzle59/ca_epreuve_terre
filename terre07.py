import sys

if len(sys.argv)==2 :

    string=sys.argv[1]

    try:
        b=int(string)
        print('erreur')
    except ValueError:
        compteur=0
        for char in string:
            compteur+=1
        print(compteur)
    # else:
    #     print("erreur")
else:
    print("erreur")
#questionnement sur le type string. quand on donne des chiffres en entrée cela
#ne doit pas fonctionner/.
#table ascii , ord ?
#autre idée: vérifier que l'argument commence par " ou ' et finit par "ou '
#plus classe je pense .
#autre solution avec cette tentative de int(). Mais ça n'empêche que pour
# 50 cela doit mettre erreur , mais pour "50" cela devrait afficher 2..
#tenté getopt , ça ne résout pas le pb. Argparse plutôt ?
#
#Apparemment les arguments en ligne de commande sont forcéments des strings,
#la solution de tenter de l'utiliser en int semble donc pertinente
