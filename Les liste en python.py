from statistics import mean
# creer une liste de stockage
# ananas,banane,pomme
fruit=["ananas","banane","pomme"]
print(fruit)
print(fruit[0])
print(fruit[2])
print(fruit[len(fruit)-1])
print(fruit)
# modifier
# pour recuperer
fruit[0]= "orange"
print(fruit)
# pour inserer une nouvelle valeur
fruit.insert(2,"credo")
print(fruit)
# pour modifier plusieur valeurs
fruit[2:4]=["jack","gabriel"]
print(fruit)
# en ajouter d'autres
# on imagine qu'un joueur "gameur123" se connecte
# pour ajouter
fruit.append("gameur123")
print(fruit)
# pour etendre
fruit.extend(["gameur2","gameur3"])
print(fruit)
# pour supprimer un element de la liste
del fruit[1]
print(fruit)
fruit.pop(0)
print(fruit)
fruit.remove("gameur2")
# si vous voulez supprimer tous elements de la liste
fruit.clear()
print(fruit)
# jouer à la maitrise 

notes=[
    1,2,3,4
       ,14,3]
print(notes)
print(notes[0])
# module statistics
resultat = mean(notes)

print("la moyenne de l'eleve est de []".format(resultat))
# pour demander à l'utilisateur
text=input("entrer une chaine de la forme (email-pseudo-motdepasse ) : ").split("-")
print(text)

# tp: generateur de phrase :
# demander en console une chaine de la forme  "mot1/mot2/mot3/mot4"
# transformer cette chaine en une liste 
# la melanger
# si le nombre d'elements de cette liste est inferieur à 10
# afficher les deux premiers mots
# si le nombre d'element est superieur ou egal à 10 
# afficher les 3 derniers
chaine=input("écrivez  une chaine de la forme'mot1/mot2/mot3/mot4' : ").split("/")
print(chaine) 
nombre=len(chaine)
print(nombre)
if nombre<10:    
    print(chaine[1])    

    print(chaine[2]) 
else :
    print(chaine[-3])
    print(chaine[-2]) 
    print(chaine[-1])
