def allPathR(lst):
    if len(lst)==1:
        return [lst]
    
    lstRes=[]
    for a in lst:
        remainLst=[x for x in lst if x!=a]
        lstRecur=allPathR(remainLst)
        print(lstRecur)


allPathR([1,2,3])
