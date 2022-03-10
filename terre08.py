import sys
if len(sys.argv[1:])==2:
    try:
        a=int(sys.argv[1])
        b=int(sys.argv[2])
        if b==0:
            print("1")
        elif b>0 :
            print(f"{a**b}")
        else:
            print("erreur")
    except ValueError:
        print("Wrong arguments")
else:
     print("erreur")
