
def getCellWidth(objectNum):
    width, height = (530, 750)
    cellWidth = width / (objectNum+1)
    return cellWidth

def getNoteWidth(objectNum):
    noteWidth = getCellWidth(objectNum) * 0.3
    return int(noteWidth)

def getNoteMultilineVerticalSpacing():
    return 15

def getMsgVerticalSpacing():
    return 50

def getLifelineX(objectNum, i):
    cellWidth = getCellWidth(objectNum)
    topX = cellWidth*i+ cellWidth*2/3
    return topX

def getPageHeight():
    return 750

def getPageInitialHeight():
    return 45