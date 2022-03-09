import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
if a>=b:
    try:
        dividende=a//b
        print(f"résultat: {dividende}")
        print(f"reste: {a%b}")
    except ZeroDivisionError:
        print("erreur.")
else:
    print("erreur.")
