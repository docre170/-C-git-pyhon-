liste=[1,2,2,3,4,4,4,5]
#index defini la position
liste.index
print(liste.index(4))
#count compte le nombre d'element
liste.count
print(liste.count(2))
#sort sert à mettre en nombre croissant 
liste.sort()
print(liste)
#reverse renverse la position des tous elements
liste.reverse()
print(liste)
jack=[10,20,30,40,50]
#pour   ajouter des elements specifique
jack.append(60)
jack.append(70)
jack.append(80)
print(jack)
#pour inserer des elements avec une position
jack.insert(3,25)
print(jack)
#pour trouver les nombres de la liste divisible par 25
jack=[ x for x in jack if x%25==0]
print(jack)
#dictionnaire appeler data frame; la definition c'est la cle
dictionnaire={
    #gabriel est la cle et nom est la valeur
    "jack":"0902324233",
    "gabriel":"0841535654",
    "rais":"0942345632",
    "herve":"0814321456",
    "esther":"0903432098",
    }

print(dictionnaire)
