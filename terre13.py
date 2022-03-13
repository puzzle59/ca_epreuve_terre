import sys
list_int=[]
right_arg=""
for integer in sys.argv[1:]:
    try :
        list_int.append(int(integer))

    except ValueError:
        right_arg="Erreur"
if right_arg=="Erreur":
    print(right_arg)
else:
    bool=True
    for i  in range(len(list_int)-1):
        if list_int[i]>list_int[i+1]:
            bool=False
    if bool:
        print("Elle est triée!")
    else:
        print("Pas triée")
