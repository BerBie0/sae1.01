def allPathR(lst):
    if len(lst)==1:
        return [lst]
    
    lstRes=[]
    for a in lst:
        remainLst=[x for x in lst if x!=a]
        lstRecur=allPathR(remainLst)
        print(lstRecur)


#allPathR([1,2,3])

def allPathRec(lst):
    if len(lst) == 1:
        return lst
    return [lst[0]] + allPathRec(lst[1:])

#print("Recu: ", allPathRec([1,2,3]))

#Question 4
# Trouver ttes les permutations
def permutation(liste):
    # Si la liste est vide alors il n'y a pas de permutations
    if len(liste) == 0:
        return []
    # Si la liste contient un élément alors il y a juste une permutation
    if len(liste) == 1:
        return [liste]
    # Sinon chercher toutes les permutations de la liste = liste!
    res = []    # liste vide pour le résultat de permutation
    # Iteration de la liste et calcul de permutation
    for i in range(len(liste)):
        #print("i=",i)
        m = liste[i]
        # Extraire liste[i] ou m de la liste. remLst est liste restante
        remLst = liste[:i] + liste[i+1:]
        # print(f"liste[:{i}]=",liste[:i])
        # print(f"liste[{i+1}:]=",liste[i+1:])
        # print("remLst=", remLst)
        # Générer ttes les permutations ou m est le premier élément
        for p in permutation(remLst):
            # print("p=", p)
            # print("m=",m)
            res.append([m] + p)
            # print("res.append([m] + p)=", res)
    return res

# Driver program to test above function
data = [1,2,3]

#print("Toutes les permutations possibles:", permutation(data))
print("Toutes les permutations possible de data=", data, "sont:")
for p in permutation(data):
    print(p)

#fonction récursive question 5
#Calculer tous les possibilités de voyage et trouvez le chemin le plus court.
#Nous considéreront que le point de départ sera le point de coordonnées [0,0]
def allPathR1(liste):
    res = []
    taille = len(liste)
    if taille == 1:
        return liste
    res = res.append(allPathR1(liste[:taille - 1]))
    return res


liste = [1,2,3]
#allPathR(liste)
#print(allPathR1(liste))
print(liste[0:len(liste)])
print(liste[0:len(liste)-1])