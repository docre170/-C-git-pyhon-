# code
pc_prix=9000
porte=int(input("entrer la somme : "))
# le prix du pc est inferieur à 1000
print(pc_prix < 1000)
# avec l'operation de comparaison la reponse sera en boolean c.à.d la reponse sera donneé en true ou false.
# pour faire une condition,nous utilisons "if","elif","else".
# if signifie "si" en francais. il est utilisé si la condition est vraie.
if pc_prix<porte and pc_prix > porte :
     print("le prix du pc est inferieur à 1000")
     porte -= pc_prix
    #  si la condition est vraie ce message afficher et une operation sera faites
else:
     print("le prix est superieur est 9000")
    #  else signifie "sinon"; il sera afficher si la condition est fausse
    # superieur(>);inferieur(<);egal(==);different(!=);superieur ou egal (>=);inferieur ou egal(<=)
    # voici un exemple de condition ternaire
text=("l'achat est possible","l'achat est possible")[pc_prix <= 1000]
print(text)
# exemple : verification de mot de passe

password=input("entrer votre mot de passe : ")
# verifier si le mot est inferieur à 8
password_length=len(password)
if password_length<8:
     print("mot de passe inferieur")
elif 8< password_length <=12:
     print("mot de passe moyen!")
else:
     print("mot de passe parfait!")
# le nombre de chiffre du password
print(password_length)

# exercice
# faire un systeme de place de cinema:
# recolter l'age de la personne "quel est votre age "
# si la personne est mineure il devra payer il paye 7$
# si la personne est majeur 12$
# souhaitez-vous de la nourriture 
# si oui +5$
# afficher ce prix

# resolution
print("bienvenu au cinema ")
place=int(input("voulez reservé une place 1 ou 0 : "))
if place==1:
     age=int(input("entrer votre age : "))
     if age>18:
          print("vous allez payez 12 $")
          repas=int(input("voulez vous du pop corn 1 ou 0 : "))
          if repas==1:
               print("plus 5 $")
               print("vous allez payez 17 $")
          else:
               print("merci ; vous allez payez 12$")
     else:
          print("vous allez 7$")
          repas=int(input("voulez vous du pop corn 1 ou O : "))
          if repas==1:
               print("plus 5 $")
               print("vous allez payer 12$")
          else:
               print("vous allez payez 7$")




