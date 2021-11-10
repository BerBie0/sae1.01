#Il faut calculer a l'origine de [0,0]
import random
import math

def createGrid(cols, rows):
    """[Function createGrid : function create an empty array(2nd). first degree contains number of rows. second degree is an array contains number of columns. size is given in argument]

    Args:
        cols ([int]): [number of columns (x)]
        rows ([int]): [number of rows (y)]

    Returns:
        [array (2nd)]: [array of 2nd which have x cols and y rows]
    """
    return [[" " for i in range(cols)] for j in range(rows)]

def randomCoord(grid):
    """[function randomCoord : function create an array(2nd). first degrees stands for the number of coord. second degree contains random pair of coord (x,y) array(1nd). 0<x<19, 0<y<49]

    Args:
        grid ([array (2nd)]): [grid without coord]

    Returns:
        [array (2nd)]: [grid with coord]
    """
    cols=len(grid[0]) #x
    rows=len(grid) #y
    for y in range(rows):
        for x in range(cols):
            if x==0:
                grid[y][x]=random.randint(0,19)
            else:
                grid[y][x]=random.randint(0,49)
    return grid

def showGrid(grid):
    """[function showGrid. The function display len(grid) then back to the line]

    Args:
        grid ([array 2nd]): [grid]
    """
    rows=len(grid) #y
    for y in range(rows):
        print(grid[y])

def addCoordToGrid(coord,grid):
    """[function addCoordToGrid. the function runs through each row of the coordinate table. it then adds an x in the grid array which corresponds one after the other to the coords of the coords array]

    Args:
        coord (array (2nd)): [array of the coords]
        grid (array (2nd)): [empty grid of the map]

    Returns:
        [array (2nd)]: [grid of the map with coords]
    """
    cols=len(coord[0]) #x
    rows=len(coord) #y
    for y in range(rows):
        grid[coord[y][1]][coord[y][0]]="x"
    return grid

def lenBetweenTwoPoints(points1,points2):
    """[function lenBetweenTwoPoints. the function calculate the distance between 2 points]

    Args:
        points1 ([array]): [array of 2 elements (x,y)]
        points2 ([array]): [array of 2 elements (x,y)]

    Returns:
        [float]: [distance between 2 points]
    """
    return math.sqrt((points1[0]-points2[0])**2 + (points1[1]-points2[1])**2)

def lenBetweenAllPoints(coord):
    """[function lenBetweenAllPoints. the function calculte the disatance between all points and save data in a matrix which as a size of the number of coords]

    Args:
        coord ([array 2nd]): [array of the coords]

    Returns:
        [array 2nd]: [matrix]
    """
    rows=len(coord) #y
    matrix=createGrid(rows,rows)
    #counter aa to track the correct insert position 
    aa=0
    for a in range(rows):
        #opti : for b in range(a,rows)
        #counter bb to track the correct insert position 
        bb=0
        for b in range(rows):
            if a==b:
                matrix[aa][bb]=lenBetweenTwoPoints([0,0],coord[a])
            else:
                matrix[aa][bb]=lenBetweenTwoPoints(coord[a],coord[b])
            bb+=1
        aa+=1
    return matrix
    """"V1
    cpt=0
    res=[]
    matrice=createGrid(8,8)
    rows=len(coord) #y
    for a in range(rows):
        #opti : for b in range(a,rows)
        for b in range(rows):
            res.append(lenBetweenTwoPoints(coord[a],coord[b]))
    for a in range(8):
        for b in range(8):
            matrice[a][b]=res[cpt]
            cpt+=1
    return matrice
    """

def allPath(coord):
    """[Function allPath. the function will calculate all possible path. it will exclude the paths that return to a destination already reached. for 8 points the function will calculate 8! path]

    Args:
        coord ([array 2nd]): [array of coord]

    Returns:
        [array 2nd]: [first degrees : number of path. second degrees : path]
    """
    res=[]
    rows=len(coord) #y
    for a in range(1,rows+1):
        for b in range(1,rows+1):
            if a!=b:
                for c in range(1,rows+1):
                    if c!=b and c!=a:
                        for d in range(1,rows+1):
                            if d!=c and d!=b and d!=a:
                                for e in range(1,rows+1):
                                    if e!=d and e!=c and e!=b and e!=a:
                                        for f in range(1,rows+1):
                                            if f!=e and f!=d and f!=c and f!=b and f!=a:
                                                for g in range(1,rows+1):
                                                    if g!=f and g!=e and g!=d and g!=c and g!=b and g!=a:
                                                        for h in range(1,rows+1):
                                                            if h!=g and h!=f and h!=e and h!=d and h!=c and h!=b and h!=a:
                                                                path=[a,b,c,d,e,f,g,h]
                                                                res.append(path)
      

                                                            
            
    return res

def allPathR2(coord):
    rows=len(coord) #y
    res=[]
    for a in range(1,rows+1):
        res.append(a)
    return res

def allPathR(lst):

    if len(lst)==1:
        return [lst]
    
    lstRes=[]
    for a in lst:
        remainLst=[x for x in lst if x!=a]
        lstRemainElement=allPathR(remainLst)
        for b in lstRemainElement:
            lstRes.append([a]+b)
    return lstRes

def lenPath(path, matrix):
    """[function lenPath. calculate the len of a path]

    Args:
        path ([array]): [array of a path]
        matrix ([array 2nd]): [matrix of len between all points]

    Returns:
        [float]: [len of the path]
    """
    totalLen=0
    for a in range(len(path)-1):
        totalLen+=matrix[path[a]-1][path[a+1]-1]
    totalLen+=matrix[path[0]-1][path[0]-1]
    totalLen+=matrix[path[7]-1][path[7]-1]
    return totalLen

def shorterPath(path, matrix):
    """[function shorterPath. calculate the shorter path of an array of path]

    Args:
        path ([array 2nd]): [array of all path]
        matrix ([array 2nd]): [matrix of len between all points]

    Returns:
        [array]: [shoter path]
    """
    res=lenPath(path[0], matrix)
    res3=path[0]
    rows=len(path)
    for a in range(rows):
        i=lenPath(path[a], matrix)
        if i<res:
            res=i
            res3=path[a]
    return res3

def addStepToGrid(grid, coord, path):
    """[function addStepToGrid. add of running order]

    Args:
        grid ([array 2nd]): [grid of the coords]
        coord ([array 2nd]): [array of the coords]
        path ([array]): [shorter path]

    Returns:
        [type]: [description]
    """
    cpt=1
    for a in path:
        grid[coord[a-1][1]][coord[a-1][0]]=str(cpt)
        cpt+=1
    return grid

matrix=[
[30.610455730027933, 19.235384061671343, 7.211102550927978, 17.08800749063506, 10.816653826391969, 18.110770276274835, 18.973665961010276, 6.4031242374328485],
[19.235384061671343, 21.0, 15.297058540778355, 9.486832980505138, 13.45362404707371, 5.0990195135927845, 9.055385138137417, 17.0],
[7.211102550927978, 15.297058540778355, 23.430749027719962, 16.97056274847714, 13.0, 16.1245154965971, 18.439088914585774, 11.0],
[17.08800749063506, 9.486832980505138, 16.97056274847714, 30.14962686336267, 7.0, 4.47213595499958, 2.0, 12.041594578792296],
[10.816653826391969, 13.45362404707371, 13.0, 7.0, 31.622776601683793, 9.848857801796104, 9.0, 5.0990195135927845],
[18.110770276274835, 5.0990195135927845, 16.1245154965971, 4.47213595499958, 9.848857801796104, 26.019223662515376, 4.0, 14.317821063276353],
[18.973665961010276, 9.055385138137417, 18.439088914585774, 2.0, 9.0, 4.0, 30.01666203960727, 14.035668847618199],
[6.4031242374328485, 17.0, 11.0, 12.041594578792296, 5.0990195135927845, 14.317821063276353, 14.035668847618199, 32.64965543462902],
]

matrix_3_3 = [
    [30,19,7],
    [19,21,9],
    [7,15,23]
]
def nearest(matrix):
    path=[]
    min=matrix[0][0]
    pos=1
    for a in range(len(matrix)):
        if matrix[a][a]<min:
            min=matrix[a][a]
            pos=a+1
    lenNear = min
    path.append(pos)
    a=0
    while len(path)<len(matrix):
        min=100
        for b in range(len(matrix[path[a]-1])):
            if (matrix[path[a]-1][b]<min) and (b+1 not in path) and (matrix[path[a]-1][b]!=matrix[b][b]):
                min=matrix[path[a]-1][b]
                pos=b+1
        path.append(pos)
        lenNear += min
        a+=1
    lenNear += matrix[path[-1]-1][path[-1]-1] #Add the distance between the last town and the origin
    print(lenNear)
    return path

print(nearest(matrix))
#print(nearest(matrix_3_3))


def main():
    coord=randomCoord(createGrid(2,8))
    
    grid=createGrid(20,50)
    grid=addCoordToGrid(coord,grid)
    
    matrix=lenBetweenAllPoints(coord)
    path=allPath(coord)
    #path2=allPathR(allPathR2(coord))
    minPath=shorterPath(path,matrix)
    #minPath2=shorterPath(path2,matrix)
    minPathNearest=nearest(matrix)
    print(minPath)
    #print(minPath2)
    print(minPathNearest)

    #showGrid(coord)
    #showGrid(grid)
    #showGrid(matrix)

    grid=addStepToGrid(grid, coord, minPath)
    #showGrid(grid)
    #print(minPath)
    

#main()
