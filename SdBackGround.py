from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib import colors
from SdGlobalConfig import *

#----------------------------------------------------------------------
#|  Feature Name                                                      |
#----------------------------------------------------------------------
#|          Module M        |        Module N        |   By: xxTeam   |
#----------------------------------------------------------------------
#|  Object A  |  Object B  |  Object C  |  Object D  |   2015.07.01   |
#----------------------------------------------------------------------
#       |    msg1   |            |           |    msg1 should be send at...
#       | --------> |            |           |
#       |           |    msg2    |           |    msg2 is send out for xx reason
#       |           | ---------> |           |
#       |           |            |    msg3   |    msg3 should take xx IE
#       |           |            | --------> |
#       |           |            |           |
#       |           |            |    msg4   |    ...
#       |           |            | <-------- |
#       |           |            |           |
#       |           |     msg5   |           |
#       |           | <--------- |           |
#       |    msg6   |            |           |
#       | <-------- |            |           |
#       |           |            |           |
#-----------------------------------------------------------------------

class SdBackGround:
    
    def __init__(self, featureName, objectList):
        self.featureName = featureName      
        self.objectList = objectList

    def draw(self, canvas):
        data = self._fillTableHeader()
        self._drawTable(canvas, data)
        self._drawLifeline(canvas)

    def _drawTable(self, canvas, data):
        cellWidth = getCellWidth(len(self.objectList)) 
        table = Table(data, cellWidth)

        table.setStyle(TableStyle([
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('ALIGNMENT', (0,1), (-1,2), 'CENTER'),
                       ('GRID', (0,1), (-1,-1), 0.25, colors.black),
                       ]))

        table.wrapOn(canvas, 10, 10)

        leftTopX, leftTopY = (30, 750)
        table.drawOn(canvas, leftTopX, leftTopY)

    def _drawLifeline(self, canvas):

        for i in range(len(self.objectList)):
            topX = getLifelineX(len(self.objectList), i)
            topY = 50
            bottomX = topX
            bottomY = 750
            canvas.line(topX, topY, bottomX, bottomY) 
            #print "lifeLine:", i, topX, topY, bottomX, bottomY

    def _fillTableHeader(self):        
        data = []
        
        #1st row: feature name 
        tableName = []
        tableName.append(self.featureName)
        data.append(tableName) 

        #2nd row: module list
        nestedItem1 = []
        for i in range(len(self.objectList)):            
            nestedItem1.append('') 
        nestedItem1.append('xLab Product')
        data.append(nestedItem1) 

        #3rd row: object list
        nestedItem2 = []    
        for i in range(len(self.objectList)):            
            nestedItem2.append(self.objectList[i])
        nestedItem2.append('2015.06.11')
        data.append(nestedItem2)
        return data

