# les listes peuvent etre modifie
beni=[]
beni=[1,2,"mbungi",True]
beni.append(4)
beni.insert(9,8)
print(beni[1])
print(beni)
beni.remove(2)
dernier=beni.pop()
beni.clear()
print(beni)
beni=20
print(beni)
# les dictionnaires les valeurs peuvent etre de tout type
archange={"nom":"kivuvu","age":24,"ville":"kinshasa"}
print(archange["age"])
archange["foi"]="chretien"
# les tuples sont souvent utilisés pour representer des collections immuables de données
fred=(1,2,3,'texte')
print(fred[1])

