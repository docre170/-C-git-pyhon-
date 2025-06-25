def dire_bonjour():
    print("Bonjour tout le monde ! :)")

dire_bonjour()
def dire(nom_personne, message_personne):
# format
    print("{} : {}".format(nom_personne,message_personne))


dire("credo", "bonjour")
dire("jack", "salut")
# il faut donner des exemples avec des jeux
def show_inventory(*list_items):
    for item in list_items:
        print(item)


show_inventory("épée")
show_inventory("épée","arc", "potion de mana" , "cape de dragon rouge")
# fonction return
def calculer_somme(nombre1, nombre2):
    return nombre1 + nombre2
print(calculer_somme(5,4))
def comparaison(nombre, nombre3):
    if nombre>nombre3:
        return nombre
    elif nombre<nombre3:
        return nombre3
    else :
        return "egalité"

print(comparaison(1,3))
print("---------------------------------------------------------------")
def difference(a,b):
    return a-b
def multiplication(c,d):
    return c*d
def division(e,f):
    return e/f
print("1. faire une somme")
print("2. faire une multiplication")
print("3. faire une division")
print("4. quitter le programme")
choix=int(input("choisir un nombre entre 1,2,3,4 : "))
if choix==1:
    print("programme qui calcule la somme")
    nombre1 =int(input("entrez un nombre : "))
    nombre2 =int(input("entrer un autre nombre : "))
    somme=calculer_somme(nombre1,nombre2)
    print(f"la somme est {somme} ")
elif choix ==2:
    print("programme qui calcule la multiplication")
    c =int(input("entrez un nombre : "))
    d =int(input("entrez un autre nombre : "))
    produit= multiplication(c,d)
    print("le produit est ",produit)
elif choix==3:
    print("programme qui calcule la multiplication")
    e =int(input("entrez un nombre : "))
    f =int(input("entrez un autre nombre : "))
    reste=division(e,f)
    print(reste)
else:
    print("A bientot")
    