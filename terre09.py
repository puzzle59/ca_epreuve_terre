import math
import sys
if len(sys.argv[1:])==1:
    try:
        number=int(sys.argv[1])
        if number >=0:
            print(f"{math.sqrt(number)}")
        else:
            print("erreur")
    except ValueError:
        print("Wrong argument type")
else:
    print("erreur")
