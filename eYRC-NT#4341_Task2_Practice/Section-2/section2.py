import numpy as np
import cv2
import math
import time

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
def readImageHSV(filePath):
    mazeImg = cv2.imread(filePath)
    hsvImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2HSV)
    return hsvImg

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
def readImageBinary(filePath):
    mazeImg = cv2.imread(filePath)
    grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)
    return binaryImage

##  Returns sine of an angle.
def sine(angle):
    return math.sin(math.radians(angle))

##  Returns cosine of an angle
def cosine(angle):
    return math.cos(math.radians(angle))

##  This function accepts the img, level and cell number of a particular cell and the size of the maze as input
##  arguments and returns the list of cells which are traversable from the specified cell.
def findNeighbours(img, level, cellnum, size):
    neighbours = []
    ############################# Add your Code Here ################################
    mazeimg=img
    height, width,col = img.shape

    r=level
    c=cellnum

    ## m represents the minimum angel of the sector at different levels


    
    if size==1:
        if level==1:
            m = (float) (1.0) * 360/6
        elif level==2:
            m = (float) (1.0) * 360/12
        else:
            m = (float) (1.0) * 360/24
    else:
        if level == 1:
            m = (float) (1.0) * 360/6
        elif level==2:
            m = (float) (1.0) * 360/12
        elif level<=5:
            m = (float) (1.0) * 360/24
        else:
            m = (float) (1.0) * 360/48
    radius = 40*(r+1)
    radius1 = 40*r
    center = (width / 2, height/2)
    axes = (radius, radius)
    angle = 0
    startAngle = m*(c-1)
    endAngle = m*c
    ma=(startAngle+endAngle)/2
    mr=(radius+radius1)/2


    ## Calculation of mid point of the walls 

    mx1=int(round(float(width/2+radius*cosine(ma))))
    my1=int(round(float(height/2+radius*sine(ma))))
    mx2=int(round(float(width/2+mr*cosine(endAngle))))
    my2=int(round(float(height/2+mr*sine(endAngle))))
    mx3=int(round(float(width/2+mr*cosine(startAngle))))
    my3=int(round(float(height/2+mr*sine(startAngle))))
    mx4=int(round(float(width/2+radius1*cosine(ma))))
    my4=int(round(float(height/2+radius1*sine(ma))))
    mx5=int(round(float(width/2+radius*cosine((ma+startAngle)/2))))
    my5=int(round(float(height/2+radius*sine((ma+startAngle)/2))))
    mx6=int(round(float(width/2+radius*cosine((ma+endAngle)/2))))
    my6=int(round(float(height/2+radius*sine((ma+endAngle)/2))))
    

    ## Crops out a very small based on coordinates and converts into binary

    ## Check the wall of the previous cell
    img1 = mazeimg[(my3)-5:(my3)+5,(mx3)-5:(mx3)+5,]
    grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret1,binaryImage1 = cv2.threshold(grayImg1,127,255,0)


    ## Checks if there is wall present by detecting the intensity 

    if binaryImage1[5][5]==255:
        if cellnum==1:
            if level==1:
                 neighbours.append((level,6))
            if level==2:
                neighbours.append((level,12))
            if level==3 or level==4 or level==5:
                neighbours.append((level,24))
            if level==6:
                neighbours.append((level,48))
        else:
            neighbours.append((level,cellnum-1))
    
    ## Check the wall of the lower level
    img2 = mazeimg[(my4)-5:(my4)+5,(mx4)-5:(mx4)+5,]
    grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret2,binaryImage2 = cv2.threshold(grayImg2,127,255,0)

    if binaryImage2[5][5]==255:
        if level==6 or level==3 or level==2:
            neighbours.append((level-1,int((cellnum+1)/2)))
        elif level==1:
            neighbours.append((level-1,0))
        else:
            neighbours.append((level-1,cellnum))
        
    ## Check the wall of the next cell
    img3 = mazeimg[(my2)-5:(my2)+5,(mx2)-5:(mx2)+5,]
    grayImg3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    ret3,binaryImage3 = cv2.threshold(grayImg3,127,255,0)

    if binaryImage3[5][5]==255:
        if level==1 and cellnum==6 : 
            neighbours.append((level,1))
        elif level==2 and cellnum==12:
            neighbours.append((level,1))
        elif level==3 and cellnum==24:
            neighbours.append((level,1))
        elif level==4 and cellnum==24:
            neighbours.append((level,1))
        elif level==5 and cellnum==24:
            neighbours.append((level,1))
        elif level==6 and cellnum==48:
            neighbours.append((level,1))
        else:
            neighbours.append((level,cellnum+1))



    ## Check the wall of the higher level
    if size==1:
        if level==3 or level==4:
            img4= mazeimg[(my1)-5:(my1)+5,(mx1)-5:(mx1)+5,]
            img5= mazeimg[(my1)-5:(my1)+5,(mx1)-5:(mx1)+5,]
        if level==2 or level==1:
            img4= mazeimg[(my5)-5:(my5)+5,(mx5)-5:(mx5)+5,]
            img5= mazeimg[(my6)-5:(my6)+5,(mx6)-5:(mx6)+5,]

    if size==2:
        if level==3 or level==4 or level==6:
            img4= mazeimg[(my1)-5:(my1)+5,(mx1)-5:(mx1)+5,]
            img5= mazeimg[(my1)-5:(my1)+5,(mx1)-5:(mx1)+5,]
        if level==1 or level==2 or level==5:
            img4= mazeimg[(my5)-5:(my5)+5,(mx5)-5:(mx5)+5,]
            img5= mazeimg[(my6)-5:(my6)+5,(mx6)-5:(mx6)+5,]
    


    grayImg4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
    ret4,binaryImage4 = cv2.threshold(grayImg4,127,255,0)
    grayImg5 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
    ret5,binaryImage5 = cv2.threshold(grayImg5,127,255,0)
    
    if binaryImage4[5][5]==255:
        if size==2:
            if level==5 or level==2 or level==1:
                neighbours.append((level+1,2*cellnum-1))
            if level==4 or level==3:
                neighbours.append((level+1,cellnum))
        if size==1:
            if level==2 or level==1:
                neighbours.append((level+1,2*cellnum-1))
            if level==3:
                neighbours.append((level+1,cellnum))


    
    
    if binaryImage5[5][5]==255:
        if size==2:
            if level==5 or level==2 or level==1:
                neighbours.append((level+1,2*cellnum))
        if size==1:
            if level==2 or level==1:
                neighbours.append((level+1,2*cellnum))
    




    #################################################################################
    return neighbours

##  colourCell function takes 5 arguments:-
##            img - input image
##            level - level of cell to be coloured
##            cellnum - cell number of cell to be coloured
##            size - size of maze
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
def colourCell(img, level, cellnum, size, colourVal):
    ############################# Add your Code Here ################################
    image1=img.copy()
    image=img
    WHITE = (255, 255, 255)
    clr = (colourVal, colourVal, colourVal)
    height, width = img.shape
    
    ## Ellipse parameters
    
    r=level
    c=cellnum
    if size==1:
        if level==1:
            m = (float) (1.0) * 360/6
        elif level==0:
            m= (float) (1.0) * 360
        elif level==2:
            m = (float) (1.0) * 360/12
        else:
            m = (float) (1.0) * 360/24
    else:
        if level == 1:
            m = (float) (1.0) * 360/6
        elif level==0:
            m= (float) (1.0) * 360
        elif level==2:
            m = (float) (1.0) * 360/12
        elif level<=5:
            m = (float) (1.0) * 360/24
        else:
            m = (float) (1.0) * 360/48

    radius = 40*(r+1)
    center = (width / 2, height/2)
    axes = (radius, radius)
    angle = 0
    startAngle = m*(c-1)
    endAngle = m*c
    ## When thickness == -1 -> Fill shape
    thickness = -1

    ##  Drawing black sector
    cv2.ellipse(image, center, axes, angle, startAngle, endAngle, clr, thickness)

    axes = (radius - 40, radius - 40)
    ## Drawing a bit smaller white sector
    cv2.ellipse(image, center, axes, angle, startAngle, endAngle,WHITE , thickness)
    img  = cv2.bitwise_and(image1,image)
    img = cv2.medianBlur(img,3)


    #################################################################################  
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph( img,size   ):      ## You can pass your own arguments in this space.
    graph = {}
    ############################# Add your Code Here ################################

    if size==1:
        ## This loop traverses all the cells in the maze of size 1 and adds the coordinates and its neighbours in graph
        for x in range(0,5):
            if x==4 or x==3:
                b=25
            if x==2:
                b=13
            if x==1:
                b=7
            if x==0:
                b=7
            for y in range(1,b):
                if x==0:
                    neighbours = findNeighbours(img, 1,y,size)
                    for z in neighbours:
                        if z==(0,0):
                            node=(0,0)
                            graph[node]=[(1,y)]
                        
                else:
                    neighbours = findNeighbours(img, x,y,size)
                    node=(x,y)
                    graph[node]=neighbours

    if size==2:

        ## This loop traverses all the cells in the maze of size 2 and adds the coordinates and its neighbours in graph
        for x in range(0,7):
            if x==6:
                b=49
            if x==5 or x==4 or x==3:
                b=25
            if x==2:
                b=13
            if x==1:
                b=7
            if x==0:
                b=7
            for y in range(0,b):
                if x==0:
                    neighbours = findNeighbours(img, 1,y,size)
                    for z in neighbours:
                        if z==(0,0):
                            node=(0,0)
                            graph[node]=[(1,y)]
                        
                else:
                    neighbours = findNeighbours(img, x,y,size)
                    node=(x,y)
                    graph[node]=neighbours



    #################################################################################
    return graph

##  Function accepts some arguments and returns the Start coordinates of the maze.
def findStartPoint(filePath, size):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
    ## Reads image
    mazeImg = cv2.imread(filePath)
    if size==1:
        for c in range(1,25):
            height =440
            width = 440
            r=4
            radius = 40*(r+1)
            m = (float) (1.0) * 360/24
            startAngle = m*(c-1)
            endAngle = m*c
            ##Gets the x-y coordinates as per the formula
            x1=int(round(float(width/2+radius*cosine(startAngle))))
            y1=int(round(float(height/2+radius*sine(startAngle))))
            x2=int(round(float(width/2+radius*cosine(endAngle))))
            y2=int(round(float(height/2+radius*sine(endAngle))))
            ## Crops out a very small based on coordinates and converts into binary
            img1 = mazeImg[((y2+y1)/2)-5:((y2+y1)/2)+5,((x2+x1)/2)-5:((x2+x1)/2)+5,]
            grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            ret1,binaryImage1 = cv2.threshold(grayImg1,127,255,0)

            ## Checks if there is wall present by detecting the intensity 
           
            if binaryImage1[5][5]==255:
                start=(4,c)
    else:
        for c in range(1,49):
            height = 600
            width = 600
            r=6
            radius = 40*(r+1)
            m = (float) (1.0) * 360/48

            startAngle = m*(c-1)
            endAngle = m*c
            ##Gets the x-y coordinates as per the formula
            x1=int(round(float(width/2+radius*cosine(startAngle))))
            y1=int(round(float(height/2+radius*sine(startAngle))))
            x2=int(round(float(width/2+radius*cosine(endAngle))))
            y2=int(round(float(height/2+radius*sine(endAngle))))
            ## Crops out a very small based on coordinates and converts into binary
            img1 = mazeImg[((y2+y1)/2)-5:((y2+y1)/2)+5,((x2+x1)/2)-5:((x2+x1)/2)+5,]
            grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            ret1,binaryImage1 = cv2.threshold(grayImg1,127,255,0)

            ## Checks if there is wall present by detecting the intensity
            
            if binaryImage1[5][5]==255:
                start=(6,c)



    #################################################################################
    return start

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath( graph,start,end,path=[]   ):             ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################

    path=path+[start]
    ## Base case
    if start== end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    ## Recursive case
    for node in graph[start]:
        if node not in path:
            newpath=findPath(graph,node,end,path)
            if newpath:
                ## Checks if newpath is shortest
                if not shortest or len(newpath) < len(shortest):
                    shortest=newpath



    #################################################################################
    return shortest

## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}
def findMarkers( filePath,image,size   ):             ## You can pass your own arguments in this space.
    list_of_markers = {}
    ############################# Add your Code Here ################################

    ## Reads image
    img = cv2.imread(filePath)
    ## List of level and no. of cells in that level
    list = [[1,6],[2,12],[3,24],[4,24],[5,24],[6,48]]
    param1 = [ 200,0,0]
    param2 = [ 255,200,200]
    param3 = [ 0,0,200]
    param4 = [ 200,200,255]
    
    ## Detects only the blue marker 
    maskBlue  = cv2.inRange(img, np.array(param1), np.array(param2))
    ## Detects only the red marker
    maskRed  = cv2.inRange(img, np.array(param3), np.array(param4))
   
    if size==1:
        ## This loop traverses all the levels and all the cells in size 1 maze for detection of blue and red markers
        for x in range(1,5):
            for y in range(1,list[x-1][1]+1):
                if x ==1:
                    level = x
                    cellnum = y
                    
                    
                    height=440
                    width = 440
                
                    # Ellipse parameters
                
                
                    r=level
                    c=cellnum
                    if size==1:
                        if level==1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        else:
                            m = (float) (1.0) * 360/24
                    else:
                        if level == 1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        elif level<=5:
                            m = (float) (1.0) * 360/24
                        else:
                            m = (float) (1.0) * 360/48
                    
                    radius = 40*(r+1)
                    radius1 = 40*r
                    startAngle = m*(c-1)
                    endAngle = m*c
                    x1=int(round(float(width/2+radius*cosine(startAngle))))
                    y1=int(round(float(height/2+radius*sine(startAngle))))
                    x2=int(round(float(width/2+radius*cosine(endAngle))))
                    y2=int(round(float(height/2+radius*sine(endAngle))))
                    x3=int(round(float(width/2+radius1*cosine(startAngle))))
                    y3=int(round(float(height/2+radius1*sine(startAngle))))
                    x4=int(round(float(width/2+radius1*cosine(endAngle))))
                    y4=int(round(float(height/2+radius1*sine(endAngle))))
                    
                    x11 = (((3*x1+x3)/4)+((3*x2+x4)/4))/2
                    y11 = (((3*y1+y3)/4)+((3*y2+y4)/4))/2
                    
                    if maskBlue[y11][x11] == 255:
                        list_of_markers['Blue']=(x,y)
                    if maskRed[y11][x11] == 255:
                        list_of_markers['Red']=(x,y)
                else:    
                    level = x
                    cellnum = y
                    
                    
                    height=440
                    width = 440
                
                    # Ellipse parameters
                
                
                    r=level
                    c=cellnum
                    if size==1:
                        if level==1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        else:
                            m = (float) (1.0) * 360/24
                    else:
                        if level == 1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        elif level<=5:
                            m = (float) (1.0) * 360/24
                        else:
                            m = (float) (1.0) * 360/48
                    
                    radius = 40*(r+1)
                    radius1 = 40*r
                    startAngle = m*(c-1)
                    endAngle = m*c
                    x1=int(round(float(width/2+radius*cosine(startAngle))))
                    y1=int(round(float(height/2+radius*sine(startAngle))))
                    x2=int(round(float(width/2+radius*cosine(endAngle))))
                    y2=int(round(float(height/2+radius*sine(endAngle))))
                    x3=int(round(float(width/2+radius1*cosine(startAngle))))
                    y3=int(round(float(height/2+radius1*sine(startAngle))))
                    x4=int(round(float(width/2+radius1*cosine(endAngle))))
                    y4=int(round(float(height/2+radius1*sine(endAngle))))
                    
                    x11 = (((x1+x3)/2)+((x2+x4)/2))/2
                    y11 = (((y1+y3)/2)+((y2+y4)/2))/2
                    
                    
                    if maskBlue[y11][x11] == 255:
                        list_of_markers['Blue']=(x,y)
                    if maskRed[y11][x11] == 255:
                        list_of_markers['Red']=(x,y)
               
    else:
        ## This loop traverses all the levels and all the cells in size 2 maze for detection of blue and red markers

        for x in range(1,7):
            for y in range(1,list[x-1][1]+1):
                if x==1:
                    level = x
                    cellnum = y
                    
                    
                    height=600
                    width = 600
                
                    # Ellipse parameters
                
                
                    r=level
                    c=cellnum
                    if size==1:
                        if level==1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        else:
                            m = (float) (1.0) * 360/24
                    else:
                        if level == 1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        elif level<=5:
                            m = (float) (1.0) * 360/24
                        else:
                            m = (float) (1.0) * 360/48
                    
                    radius = 40*(r+1)
                    radius1 = 40*r
                    startAngle = m*(c-1)
                    endAngle = m*c
                    x1=int(round(float(width/2+radius*cosine(startAngle))))
                    y1=int(round(float(height/2+radius*sine(startAngle))))
                    x2=int(round(float(width/2+radius*cosine(endAngle))))
                    y2=int(round(float(height/2+radius*sine(endAngle))))
                    x3=int(round(float(width/2+radius1*cosine(startAngle))))
                    y3=int(round(float(height/2+radius1*sine(startAngle))))
                    x4=int(round(float(width/2+radius1*cosine(endAngle))))
                    y4=int(round(float(height/2+radius1*sine(endAngle))))
                    
                    x11 = (((3*x1+x3)/4)+((3*x2+x4)/4))/2
                    y11 = (((3*y1+y3)/4)+((3*y2+y4)/4))/2
                    
                    if maskBlue[y11][x11] == 255:
                        list_of_markers['Blue']=(x,y)
                    if maskRed[y11][x11] == 255:
                        list_of_markers['Red']=(x,y)
                
                else:
                    level = x
                    cellnum = y
                    
                    
                    height=600
                    width = 600
                
                    # Ellipse parameters
                
                
                    r=level
                    c=cellnum
                    if size==1:
                        if level==1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        else:
                            m = (float) (1.0) * 360/24
                    else:
                        if level == 1:
                            m = (float) (1.0) * 360/6
                        elif level==2:
                            m = (float) (1.0) * 360/12
                        elif level<=5:
                            m = (float) (1.0) * 360/24
                        else:
                            m = (float) (1.0) * 360/48
                    
                    radius = 40*(r+1)
                    radius1 = 40*r
                    startAngle = m*(c-1)
                    endAngle = m*c
                    x1=int(round(float(width/2+radius*cosine(startAngle))))
                    y1=int(round(float(height/2+radius*sine(startAngle))))
                    x2=int(round(float(width/2+radius*cosine(endAngle))))
                    y2=int(round(float(height/2+radius*sine(endAngle))))
                    x3=int(round(float(width/2+radius1*cosine(startAngle))))
                    y3=int(round(float(height/2+radius1*sine(startAngle))))
                    x4=int(round(float(width/2+radius1*cosine(endAngle))))
                    y4=int(round(float(height/2+radius1*sine(endAngle))))
                    
                    x11 = (((x1+x3)/2)+((x2+x4)/2))/2
                    y11 = (((y1+y3)/2)+((y2+y4)/2))/2
                    
                    
                    if maskBlue[y11][x11] == 255:
                        list_of_markers['Blue']=(x,y)
                    if maskRed[y11][x11] == 255:
                        list_of_markers['Red']=(x,y)
                   



    #################################################################################
    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the START cell and traverse to any one of the markers ( either blue or red ) and then
## traverse to FINISH. The length of path should be shortest ( most optimal solution).
def findOptimumPath( graph,start,end,list_of_markers,path=[]    ):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
    pathArray = []
    path1= []
    path2= []
    
    ## Gets all markers
    markers=list_of_markers

    ## Path1 gets path from Start->Blue->End
    path1.append(findPath(graph, start, markers['Blue']))
    path1.append(findPath(graph, markers['Blue'],end))

    ## Path2 gets path from Start->Red->End
    path2.append(findPath(graph, start, markers['Red']))
    path2.append(findPath(graph, markers['Red'],end))
    
    ## Checks if the path 1 is shorter or path 2 
    if(len(path1[0]+path1[1])<=len(path2[0]+path2[1])):
        pathArray=path1
    else: 
        pathArray=path2



    #################################################################################
    return pathArray

## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.
def colourPath(  img,path,size   ):   ## You can pass your own arguments in this space. 
    ############################# Add your Code Here ################################


    ## Loop to paint the solution path.
    for i in path:         
        for j in i:
            img = colourCell(img, j[0], j[1],size, 230)

    



    #################################################################################
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
    img = readImageHSV(filePath)
    imgBinary = readImageBinary(filePath)
    if len(img) == 440:
        size = 1
    else:
        size = 2
    listofMarkers = findMarkers( filePath,imgBinary,size  )
    path = findOptimumPath( buildGraph(cv2.imread(filePath), size),findStartPoint(filePath, size),(0,0),listofMarkers  )
    img = colourPath( imgBinary, path,size     )
    print path
    print listofMarkers
    if __name__ == "__main__":                    
        return img
    else:
        if flag == 0:
            return path
        elif flag == 1:
            return str(listofMarkers) + "\n"
        else:
            return img
    
## The main() function is called here. Specify the filepath of image in the space given.
if __name__ == "__main__":
    filePath = "image_10.png"     ## File path for test image
    img = main(filePath)           ## Main function call
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
