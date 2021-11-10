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


# Trouver ttes les permutations
def permutation(liste):
    # Si la liste est vide alors il n'y a pas de permutations
    if len(liste) == 0:
        return []
    # Si la liste contient un élément alors il y a juste une permutation
    if len(liste) == 1:
        return [liste]
    # Sinon chercher toutes les permutations de la liste= liste!
    res = []    # liste vide pour le résultation de permutation
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(liste)):
        m = liste[i]
        # Extract liste[i] or m from the list. remLst is
        # remaining list
        remLst = liste[:i] + liste[i+1:]
        print(f"liste[:{i}]=",liste[:i])
        print(f"liste[{i+1}:]=",liste[i+1:])
        print("remLst=", remLst)
        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            print("p=", p)
            print("m=",m)
            res.append([m] + p)
            print("res.append([m] + p)=", res)
    return res

# Driver program to test above function
data = [1,2,3]
# for p in permutation(data):
#     print(p)

print(permutation(data))
