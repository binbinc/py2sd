from reportlab.pdfgen.canvas import Canvas  
from reportlab.lib.units import inch    
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from SdGlobalConfig import *

class SdMessage:
    
    def __init__(self, objectNum, name, senderInx, receiverInx, detail):
        self.objectNum = objectNum
        self.name = name
        self.senderInx = senderInx
        self.receiverInx = receiverInx
        self.detail = detail

    def draw(self, canvas, bothY):
        self._drawMsgName(canvas, bothY)
        self._drawMsgArrow(canvas, bothY)
        self._drawMsgTinyNote(canvas, bothY)
        self._drawMsgDetailNote(canvas, bothY)
 
    def _drawMsgName(self, canvas, bothY):
        beginX = getLifelineX(self.objectNum, self.senderInx)
        endX = getLifelineX(self.objectNum, self.receiverInx)
        middleX = (beginX + endX) / 2

        canvas.drawCentredString(middleX, bothY, self.name)

    def _drawMsgArrow(self, canvas, bothY):
        beginX = getLifelineX(self.objectNum, self.senderInx)
        endX = getLifelineX(self.objectNum, self.receiverInx)

        if (self.senderInx < self.receiverInx):
            beginX = getLifelineX(self.objectNum, self.senderInx)#   2*self.senderInx*inch
            beginY = bothY
            endX = getLifelineX(self.objectNum, self.receiverInx)#2*self.receiverInx*inch
            endY = bothY
            canvas.line(beginX, beginY, endX, endY) 
            p = canvas.beginPath()
            p.moveTo(endX, endY)
            p.lineTo(endX-0.1*inch, endY-0.1*inch)
            p.lineTo(endX-0.1*inch, endY+0.1*inch)
            p.lineTo(endX, endY)  
            canvas.drawPath(p, stroke=1, fill=1)          
        else:
            endX = getLifelineX(self.objectNum, self.senderInx)#2*self.senderInx*inch
            endY = bothY
            beginX = getLifelineX(self.objectNum, self.receiverInx)#2*self.receiverInx*inch
            beginY = bothY
            canvas.line(beginX, beginY, endX, endY)  
            p = canvas.beginPath()
            p.moveTo(beginX, beginY)
            p.lineTo(beginX+0.1*inch, beginY-0.1*inch)
            p.lineTo(beginX+0.1*inch, beginY+0.1*inch)
            p.lineTo(beginX, beginY)  
            canvas.drawPath(p, stroke=1, fill=1)      

    def _drawMsgTinyNote(self, canvas, bothY):
        pass        

    def _drawMsgDetailNote(self, canvas, bothY):
        stylesheet = getSampleStyleSheet()
        normalStyle = stylesheet['Code']
        noteWidth = getNoteWidth(self.objectNum)
        t = Preformatted(self.detail,normalStyle,maxLineLength=noteWidth, newLineChars='')
        frags = t.lines
        n = len(frags)
        for l in range(n):
            canvas.drawString(360, bothY-l*getNoteMultilineVerticalSpacing(), frags[l])
                
    def getHeight(self):
        stylesheet = getSampleStyleSheet()
        normalStyle = stylesheet['Code']
        noteWidth = getNoteWidth(self.objectNum)
        t = Preformatted(self.detail,normalStyle,maxLineLength=noteWidth, newLineChars='')
        frags = t.lines
        n = len(frags)
        return n*getNoteMultilineVerticalSpacing()+getMsgVerticalSpacing()
