import numpy as np
import cv2

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
def readImageHSV(filePath):
    #############  Add your Code here   ###############
    img = cv2.imread(filePath)
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    ###################################################
    return hsvImg

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
def readImageBinary(filePath):
    #############  Add your Code here   ###############

    img1 = cv2.imread(filePath)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############

    img_binaryimage = img[(row)*20:((row)*20)+20,(column)*20:((column)*20)+20]
    if img_binaryimage[10][0] == 255:
        neighbours.append((row,column-1))
    if img_binaryimage[0][10] == 255:
        neighbours.append((row-1,column))
    if img_binaryimage[10][19] == 255:
        neighbours.append((row,column+1))
    if img_binaryimage[19][10] == 255:
        neighbours.append((row+1,column))


    ###################################################
    return neighbours

##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
##  You can change the colourCell() functions used in the previous sections to suit your requirements.

def colourCell(img,row,column,colourVal):   ## Add required arguments here.
    
    #############  Add your Code here   ###############

    r=row
    c=column
    cv2.rectangle(img,(c*20+2,r*20+2),((c+1)*20-2,(r+1)*20-2),(colourVal,colourVal,colourVal),-1)



    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph(img):  ## You can pass your own arguments in this space.
    graph = {}
    #############  Add your Code here   ###############

    breadth = len(img)/20       
    length = len(img[0])/20

    for x in range(0,length):
        for y in range(0,breadth):
            neighbours = findNeighbours(img, x,y)
            node=(x,y)
            graph[node]=neighbours
            



    ###################################################

    return graph

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(graph,start,end,path=[]): ## You can pass your own arguments in this space.
    #############  Add your Code here   ###############

    path=path+[start]
    if start== end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath=findPath(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest=newpath


    

    ###################################################
    return shortest     

## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}

def findMarkers(img):    ## You can pass your own arguments in this space.
    list_of_markers = {}
    #############  Add your Code here   ###############

    breadth = len(img)/20       
    length = len(img[0])/20
    param1 = [ 200,0,0]
    param2 = [ 255,200,200]
    param3 = [ 0,200,0]
    param4 = [ 200,255,200]
    param5 = [ 0,0,200]
    param6 = [ 200,200,255]
    param7 = [ 200,0,200]
    param8 = [ 255,200,255]

    maskBlue  = cv2.inRange(img, np.array(param1), np.array(param2))
    maskGreen  = cv2.inRange(img, np.array(param3), np.array(param4))
    maskRed  = cv2.inRange(img, np.array(param5), np.array(param6))
    maskPink  = cv2.inRange(img, np.array(param7), np.array(param8))
#     cv2.imshow('blue',maskBlue)
#     cv2.imshow('green',maskGreen)
#     cv2.imshow('pink',maskPink)
#     cv2.imshow('red',maskRed)
    
    for x in range(0,length):
        for y in range(0,breadth):
            binary_blue = maskBlue[(x)*20:((x)*20)+20,(y)*20:((y)*20)+20]
            if binary_blue[10][10] == 255:
                list_of_markers['Blue']=(x,y)
                
            binary_green = maskGreen[(x)*20:((x)*20)+20,(y)*20:((y)*20)+20]
            if binary_green[10][10] == 255:
                list_of_markers['Green']=(x,y)
                
            binary_pink = maskPink[(x)*20:((x)*20)+20,(y)*20:((y)*20)+20]
            if binary_pink[10][10] == 255:
                list_of_markers['Pink']=(x,y)
                
            binary_red = maskRed[(x)*20:((x)*20)+20,(y)*20:((y)*20)+20]
            if binary_red[10][10] == 255:
                list_of_markers['Red']=(x,y)
    
    ###################################################
    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the bottom left corner of the maze, collect all the markers by traversing to them and
## then traverse to the top right corner of the maze.

def findOptimumPath(graph,start,end,list_of_markers):     ## You can pass your own arguments in this space.
    path_array = []
    #############  Add your Code here   ###############

    
    markers={}
    markers=list_of_markers
    f=0
    while len(markers)!=0:
        for x in markers:
            path=findPath(graph,start,markers[x])
            if f==0:
                short=path
                f=1
            if len(path)<=len(short):
                short=path
                m=x
                
                

        
        start=markers[m]
        del markers[m]
        path_array.append(short)
        f=0
        

    lpath=findPath(graph,start,end)
    path_array.append(lpath)




    


    ###################################################
    return path_array
        
## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.

def colourPath( filePath,img,path   ):      ## You can pass your own arguments in this space. 
    #############  Add your Code here   ###############



    for i in path:         ## Loop to paint the solution path.
        for j in i:
            img = colourCell(img, j[0], j[1], 200)

    
    listOfMarkers = findMarkers(cv2.imread(filePath))
    
    for i in listOfMarkers:         ## Loop to paint the solution path.
        x,y=listOfMarkers[i]
        img = colourCell(img, x, y, 0)
    



    ###################################################
    return img

#####################################    Add Utility Functions Here   ###################################
##                                                                                                     ##
##                   You are free to define any functions you want in this space.                      ##
##                             The functions should be properly explained.                             ##




##                                                                                                     ##
##                                                                                                     ##
#########################################################################################################

## This is the main() function for the code, you are not allowed to change any statements in this part of
## the code. You are only allowed to change the arguments supplied in the findMarkers(), findOptimumPath()
## and colourPath() functions.

def main(filePath, flag = 0):
    imgHSV = readImageHSV(filePath)                ## Acquire HSV equivalent of image.
    listOfMarkers = findMarkers(cv2.imread(filePath))             ## Acquire the list of markers with their coordinates.
    test = str(listOfMarkers)
    imgBinary = readImageBinary(filePath)          ## Acquire the binary equivalent of image.
    initial_point = ((len(imgBinary)/20)-1,0)      ## Bottom Left Corner Cell
    final_point = (0, (len(imgBinary[0])/20) - 1)  ## Top Right Corner Cell
    pathArray = findOptimumPath(buildGraph(imgBinary),initial_point,final_point,listOfMarkers) ## Acquire the list of paths for optimum traversal.
    print pathArray
    img = colourPath(filePath,imgBinary, pathArray)         ## Highlight the whole optimum path in the maze image
    if __name__ == "__main__":                    
        return img
    else:
        if flag == 0:
            return pathArray
        elif flag == 1:
            return test + "\n"
        else:
            return img
## Modify the filepath in this section to test your solution for different maze images.           
if __name__ == "__main__":
    filePath = "maze00.jpg"                        ## Insert filepath of image here
    img = main(filePath)                 
    cv2.imshow("canvas", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
