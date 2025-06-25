s=0 
for i in range(8):
    nombre=int(input(" entrez un nombre : "))
    if nombre<0 :
        break
    s=s+nombre
print("la somme est : ", s)
# exercice 2
somme = 0
for i in range(8):
    n=int(input("entrer un nombre : "))
    if n <0:
        continue
    somme = somme + n
print("la somme est : ", somme)
    