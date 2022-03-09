import sys
if len(sys.argv)>=2:
    string=sys.argv[1]
    reverse_string=""
    pivot_list=[]
    if type(string)== str:
        for char in string:
            pivot_list.append(char)
        for i in range(len(pivot_list)):
            reverse_string+=(pivot_list[-i-1])
        print(reverse_string)
    else:
        print("argument must be a string")
else:
    print("erreur")
#éventuelles erreurs d'argument ?? 
