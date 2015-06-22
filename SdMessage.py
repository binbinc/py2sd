from reportlab.pdfgen.canvas import Canvas  
from reportlab.lib.units import inch    

class SdMessage:
    
    def __init__(self, name, senderInx, receiverInx, index, detail):
        self.name = name
        self.senderInx = senderInx
        self.receiverInx = receiverInx
        self.index = index
        self.detail = detail

    def draw(self, canvas):
        strPos = (2*self.senderInx + 2*self.receiverInx) / 2
        canvas.drawCentredString(strPos*inch, (10.5-1*self.index)*inch, self.name)
        print "vertial pos: ",   strPos*inch
        canvas.drawString(360, (10.5-1*self.index)*inch, self.detail)          
        if (self.senderInx < self.receiverInx):
            beginX = 2*self.senderInx*inch
            beginY = (10.5-1*self.index)*inch
            endX = 2*self.receiverInx*inch
            endY = (10.5-1*self.index)*inch
            canvas.line(beginX, beginY, endX, endY) 
            p = canvas.beginPath()
            p.moveTo(endX, endY)
            p.lineTo(endX-0.1*inch, endY-0.1*inch)
            p.lineTo(endX-0.1*inch, endY+0.1*inch)
            p.lineTo(endX, endY)  
            canvas.drawPath(p, stroke=1, fill=1)          
        else:
            endX = 2*self.senderInx*inch
            endY = (10.5-1*self.index)*inch
            beginX = 2*self.receiverInx*inch
            beginY = (10.5-1*self.index)*inch
            canvas.line(beginX, beginY, endX, endY)  
            p = canvas.beginPath()
            p.moveTo(beginX, beginY)
            p.lineTo(beginX+0.1*inch, beginY-0.1*inch)
            p.lineTo(beginX+0.1*inch, beginY+0.1*inch)
            p.lineTo(beginX, beginY)  
            canvas.drawPath(p, stroke=1, fill=1)                   
