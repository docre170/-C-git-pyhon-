# notion des erreurs en python: on distingue 3 types d'erreur:
# . syntaxique(erreur dans l'ecriture du code)
# .sémantique(lorsque)
# .logique
def inverse(x):
    y=1.0/x
    return y

try:
    a=inverse(2)
    print(a)
    b=inverse(0)
    print(b)

except:
   print("le programme à declenché une erreur") 