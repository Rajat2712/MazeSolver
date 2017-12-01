import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
## You can copy the code you wrote for section1.py here.
def readImage(filePath):
    #############  Add your Code here   ###############


    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
## You can copy the code you wrote for section1.py here.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############


    ###################################################
    return neighbours

##  colourCell function takes 4 arguments:-
##            img - input image
##            row - row coordinates of cell to be coloured
##            column - column coordinates of cell to be coloured
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
##  You can copy the code you wrote for section1.py here.
def colourCell(img,row,column,colourVal):
    #############  Add your Code here   ###############


    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph():  ## You can pass your own arguments in this space.
    graph = {}
    #############  Add your Code here   ###############


    ###################################################

    return graph

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(): ## You can pass your own arguments in this space.
    #############  Add your Code here   ###############


    ###################################################
    return shortest

## This is the main function where all other functions are called. It accepts filepath
## of an image as input. You are not allowed to change any code in this function.
def main(filePath, flag = 0):                 
    img = readImage(filePath)      ## Read image with specified filepath.
    breadth = len(img)/20          ## Breadthwise number of cells
    length = len(img[0])/20           ## Lengthwise number of cells
    if length == 10:
        initial_point = (0,0)      ## Start coordinates for maze solution
        final_point = (9,9)        ## End coordinates for maze solution    
    else:
        initial_point = (0,0)
        final_point = (19,19)
    graph = buildGraph(    )       ## Build graph from maze image. Pass arguments as required.
    shortestPath = findPath(    )  ## Find shortest path. Pass arguments as required.
    print shortestPath             ## Print shortest path to verify
    string = str(shortestPath) + "\n"
    for i in shortestPath:         ## Loop to paint the solution path.
        img = colourCell(img, i[0], i[1], 200)
    if __name__ == '__main__':     ## Return value for main() function.
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph

## The main() function is called here. Specify the filepath of image in the space given.            
if __name__ == '__main__':
    filePath = 'maze00.jpg'        ## File path for test image
    img = main(filePath)           ## Main function call
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




