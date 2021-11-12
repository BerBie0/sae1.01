#Il faut calculer a l'origine de [0,0]
import random
import math

#question 2
def createGrid(cols, rows):
    """[Function createGrid : function create an empty array(2nd). first degree contains number of rows. second degree is an array contains number of columns. size is given in argument]

    Args:
        cols ([int]): [number of columns (x)]
        rows ([int]): [number of rows (y)]

    Returns:
        [array (2nd)]: [array of 2nd which have x cols and y rows]
    """
    return [[" " for i in range(cols)] for j in range(rows)]

#question 1
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

#question 2
def showGrid(grid):
    """[function showGrid. The function display len(grid) then back to the line]

    Args:
        grid ([array 2nd]): [grid]
    """
    for i in grid:
        print(i)

#question 2
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

#question 3
def lenBetweenTwoPoints(points1,points2):
    """[function lenBetweenTwoPoints. the function calculate the distance between 2 points]

    Args:
        points1 ([array]): [array of 2 elements (x,y)]
        points2 ([array]): [array of 2 elements (x,y)]

    Returns:
        [float]: [distance between 2 points]
    """
    return math.sqrt((points1[0]-points2[0])**2 + (points1[1]-points2[1])**2)

#question 3
def lenBetweenAllPoints(coord):
    """[function lenBetweenAllPoints. the function calculte the disatance between all points and 
    save data in a matrix which as a size of the number of coords]

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

#question 4
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

#question 6
def allPathR2(coord):
    """[summary]

    Args:
        coord ([array 2nd]): [array of coord]

    Returns:
        [array]: [array of number of coords]
    """
    rows=len(coord) #y
    res=[]
    for a in range(1,rows+1):
        res.append(a)
    return res

#question 6
def allPathR(lst):
    """[summary]

    Args:
        lst ([array]): [array of number of coords]

    Returns:
        [array 2nd]: [array of all path]
    """
    if len(lst)==1:
        return [lst]
    
    lstRes=[]
    for a in lst:
        remainLst=[x for x in lst if x!=a]
        lstRemainElement=allPathR(remainLst)
        for b in lstRemainElement:
            lstRes.append([a]+b)
    return lstRes

#question 5
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

#question 5
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
    print(res)
    return res3

#question 6
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

#question 7
def nearest(matrix):
    """[summary]

    Args:
        matrix ([array 2nd]): [matrix 8*8]

    Returns:
        [array]: [shorter path]
    """
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

def affichage(grid):

    res=''
    for i in range (len(grid)):
        res+="-".join(grid[i])+'\n'
    return res

#main
def main():
    #create random coord
    coord=randomCoord(createGrid(2,8))
    coord=[[4, 4], [9, 37], [10, 8], [11, 40], [14, 29], [4, 35], [8, 16], [3, 16]]

    #create empty grid
    grid=createGrid(20,50)
    grid=addCoordToGrid(coord,grid)
    
    #create matrix 8*8
    matrix=lenBetweenAllPoints(coord)

    #generate all path
    path=allPath(coord)

    #___shortest path___
    #naive version :
    minPath=shorterPath(path,matrix)
    print(minPath)

    #recursive version :
    #path2=allPathR(allPathR2(coord))
    #minPath2=shorterPath(path2,matrix)

    #nearest version :
    #minPathNearest=nearest(matrix)

    #___display intermediate___
    #showGrid(coord)
    #showGrid(grid)
    #showGrid(matrix)

    #add step to the grid and final display
    grid=addStepToGrid(grid, coord, minPath)
    showGrid(grid)

    print(affichage(grid))
    
    

if __name__=="__main__":
    main()

