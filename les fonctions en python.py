# pour definir une fonction il d'abord utiliser le clé "def" 
def welcome():
    print("bienvenu dans tecno-world")
    resultat=1+2
    print("le resultat du calcul est ",resultat)
# por lire la fonction 
welcome()
# deuxieme fonction
def next_year():
    global year
    print("Fin de l'annee ", year) 
    year+=1
    print("debut de l'année",year)
year=2024
next_year()

# calcul 
def addition4():
    result=5+5
    return result
def multiplication():
    result =5*5
    return result
print("le resultat est",multiplication())

print("le resultat du calcul est",addition4())
def division():
    return 25//5
print("la reponse est",division())
# utilisation de parametre
def addition1():
        return 5+35
print("le resultat du calcul est",addition1())
def addition2():
         return 5+15
print("le resultat du calcul est",addition2())

def addition3():
         return 5+25
print("le resultat du calcul est",addition3())
# pour plusier calcul à la fois ; parametre et argument
def addition(n):
      return 5+n
print("le resultat du calcul est",addition(5))
print("le resultat du calcul est",addition(35))
print("le resultat du calcul est",addition(15))
print("le resultat du calcul est",addition(25))
# creer une fonction max() qui va renvoyer le resultat le plus haut parmis 2 valeurs
def max(a,b):
      if a>b:
            return a
      else:
            return b

premier_valeur=int(input("entrer un nombre a : "))
deuxieme_valeur=int(input("entrer un nombre b : "))
max_valeur=max(premier_valeur,deuxieme_valeur)
print("la valeur max est", max(premier_valeur,deuxieme_valeur))
# notin de recursivité
def add(a):
      a+=1
      print(a)
      if a<10:
            add(a)
add(2)
# travaux pratique
# tp: une fonction pour calculer le nombre de voyelles dans un mot
# definir une fonction get_vowels_numbers(mot)
# creér chaque lettres du mot vous verifiez s'il s'agit d'un voyelle
# si c'est le cas , on ajoute un au compteur
# à la fin de la fonction , vous allez renvoyez le compteur

def get_vowels_numbers(mot):
      voyelles=input("entrer un mot : ")
      compteur=0
      for lettre in mot:
            if lettre in voyelles:
                  compteur+=1
      return compteur
print("le nombre de voyelle est ",get_vowels_numbers("mot"))
