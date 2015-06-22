from reportlab.pdfgen.canvas import *  
from reportlab.lib.units import inch    

class SdObject:
	
    def __init__(self, name, x):
        self.name = name
        self.x = x
 
    def draw(self, canvas):
        canvas.drawCentredString(2*self.x*inch, 10*inch, self.name)  
        canvas.line(2*self.x*inch, 1*inch, 2*self.x*inch, 10*inch) 