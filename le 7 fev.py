argent=10
def ajouter_argent(montant):
    global argent,i
    argent += montant
    i=20
ajouter_argent(100)
print(argent)
print(i)
def count():
    n=0

    def increment():
        nonlocal n
        n += 1
        return n
    return increment
counter = count()
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
