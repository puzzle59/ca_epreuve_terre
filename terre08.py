import sys
if len(sys.argv[1:])==2:
    try:
        a=int(sys.argv[1])
        b=int(sys.argv[2])
        if b==0:
            print("1")
        elif b>0 :
            puissance=1
            for i in range(b):
                puissance=puissance*a
            print(f"{puissance}")
        else:
            print("erreur")
    except ValueError:
        print("Wrong arguments")
else:
     print("erreur")
