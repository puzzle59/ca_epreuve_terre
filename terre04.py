import sys
if len(sys.argv)>=2:
    try :
        argument=int(sys.argv[1])
        if argument % 2 == 0 :
            print("pair")
        else:
            print("impair")
    except ValueError:
        print("Tu ne me la mettras pas à l'envers")
else :
    print("Tu ne me la mettras pas à l'envers")
#note: quand on passe ";" en argument ça scinde les instructions en deux
#ex : 45;m  .. il croit que m est une commande
