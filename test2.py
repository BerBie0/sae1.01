#import main.py #NE MARCHE PAS POUR LE MOMENT
def allPathR(lst):
    if len(lst)==1:
        return [lst]
    
    lstRes=[]
    for a in lst:
        remainLst=[x for x in lst if x!=a]
        lstRecur=allPathR(remainLst)
        print(lstRecur)

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