inscrit=[]
print("bienvenu dans ce programme")
print("1.permettre a un nouveau etudiant de s'ajouter")
print("2.afficher la liste des etudiants")
print("3.filtrer les etudiants par filiere")
print("4.supprimer un etudiant de la liste si necessaire")
choix=int(input("choissisez un nombre entre 1,2,3,4 pour continuer selon le nombre de reference ci-dessus : "))
if choix=="1":
    nom=("ecrivez votre nom : ")
    filiere=("entrez votre filiere : ")
    inscrit.append({"nom": nom, "filiere": filiere})
    print(f"{nom} bienvenu dans le club.")
elif choix=="2":
       for etudiant in inscrit:
           print(f"nom : {etudiant['nom']}, filiere :{etudiant['filiere']}")


