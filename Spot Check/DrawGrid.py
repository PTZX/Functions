# define functions

def getGridSize():
    validGrid = 0
    thisGridSize = 0
    validGrid = False
    while validGrid == False:
        thisGridSize = int(input("Please enter the size of the grid (Max 20): "))
        if thisGridSize <= 20: ##and thisGridSize >=1:
            validGrid = True
    return thisGridSize
    
def GetGridRow(aRowLength):#aRowLength):
    # draws a single row using |_ for each square
    thisRow = '|_' * (aRowLength)
    # add closing | to row
    thisRow = thisRow + '|'
    return thisRow

def DisplayGrid(thisGridSize, aRow):
    # display top of grid using _ as top of each square
    print(' _' * thisGridSize)
    # display rows of |_| for each row
    for rowCount in range(thisGridSize):
        print(aRow)
    
# main program
thisGridSize = getGridSize()
rowToDraw = GetGridRow(thisGridSize)
DisplayGrid(thisGridSize, rowToDraw)
