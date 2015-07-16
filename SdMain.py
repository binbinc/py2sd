from reportlab.pdfgen.canvas import Canvas  
from SdParser import * 
from SdShuttlePage import * 

if __name__ == "__main__":

    #load textual sequence diagram
    fParser = SdParser("demo.txt")
    fParser.load()

    #ready to generate pdf   
    can = Canvas('demo.pdf')  

    #startUp shuttle pages
    xPage = SdShuttlePage(can, fParser)
    xPage.run()
