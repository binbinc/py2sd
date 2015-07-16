from reportlab.pdfgen.canvas import *  
from SdBackGround import *
from SdMessage import *
from SdGlobalConfig import *

class SdShuttlePage:
    
    def __init__(self, canvas, fParser):
        self.canvas = canvas
        self.fParser = fParser      
        self.currentPageHeight = getPageInitialHeight()
        
    def run(self):
        pageOverload = False
        for i in range(len(self.fParser.msgList)):
            if self.isEmptyCar():
                xBG = SdBackGround(self.fParser.featureName, self.fParser.objList)
                xBG.draw(self.canvas)

            pageOverload = self._tryToPickUp(self.fParser.msgList[i])
            if pageOverload:
                self.canvas.showPage()                      
                self.canvas.save() 
                self.reset()
                
        self.canvas.showPage()                      
        self.canvas.save() 

    def _tryToPickUp(self, msg):

        senderInx = self.fParser.objList.index(msg[0])
        receiverInx = self.fParser.objList.index(msg[1])   
        obj = SdMessage(len(self.fParser.objList), msg[2], senderInx, receiverInx, msg[3])
        
        pageOverload = self.needToMakeNewPage(obj.getHeight())

        if pageOverload:
            pass
        else:
            obj.draw(self.canvas, getPageHeight()-self.currentPageHeight)
            self.currentPageHeight += obj.getHeight()
        return  pageOverload  

    def needToMakeNewPage(self, expectedHeight):
        if ((self.currentPageHeight + expectedHeight) >= getPageHeight()):
            return True
        else:            
            return False

    def reset(self):
        self.currentPageHeight = getPageInitialHeight()

    def isEmptyCar(self):
        return self.currentPageHeight == getPageInitialHeight()

