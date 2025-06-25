print("hello,world")
entre=int(input("entree un nombre : "))
deuxieme=int(input("entree un second nombre : "))
som=entre+deuxieme
dif=entre-deuxieme
mult=entre*deuxieme
div=entre/deuxieme
print("la somme est ",som)
print("la difference est",dif)
print("le produit est",mult)
print("le reste est",div)
fact=entre^entre
print(fact)
annee=int(input("entrer votre annee de naissance : "))
print(annee)
actuel=int(input("entrer l annee actuelle : "))
print(actuel)
age=actuel-annee
print("vous etes age de ",age)
if age>18 :
    print("vous etes majeur")
else:
    print("vous etes mineur")
cap=int(input(" entrer le capital mise : "))
taux=float(input("entrer le taux : "))
heure=int(input("ecrit le nombre d heure : "))
interet=(cap*taux*heure)/100
print(interet)
print(entre)
if entre< 0 :
    print("ecriver un nombre positif")
elif entre==0 :
    print("le factoriel de 0 EST 1")
else :
    fact= entre>0
    print("le factoriel est ", fact)
