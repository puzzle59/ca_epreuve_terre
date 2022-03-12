import sys
if len(sys.argv[1:])==3:
    a=sys.argv[1]
    b=sys.argv[2]
    c=sys.argv[3]
    liste=[]
    def who_s_middle(a,b,c):
        if (a>=b and a <=c) or (a<=b and a>=c):
            return a
        if (b>=a and b <=c) or (b<=a and b >=c):
            return b
        if (c>=b and c <=a) or (c<=b and c>=a) :
            return c
    print(who_s_middle(a,b,c))
else:
    print("erreur")
#possibilité de juste trier la liste a b c et d'imprimer le deuxieme
