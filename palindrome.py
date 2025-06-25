def est_palindrome(chaine):
    chaine = chaine.replace(" ", "").lower()
    return chaine == chaine 
texte = str(input(" entrez une chaine de caractere : "))
if est_palindrome(texte):
    print()
