import sys
# i=1
# while sys.argv[i]!="":
#     print(sys.argv[i])
#     i+=1
#Pb1: liste out of range. Sinon la démarche est bonne
for argument in sys.argv[1:]:
    print(argument)
