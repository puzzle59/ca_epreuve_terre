alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_string=""
for lettre in alphabet:
    alphabet_string+=lettre
print(alphabet_string)
print("\n")
#Problème 1: les lettres s'affichent lignes par lignes, je les veux en une seule
#Idée : enlever l'option passage à la ligne de print ? Ce que j'ai fait pour le moment me semble
#un peu artificiel
