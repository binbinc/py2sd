from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, SimpleDocTemplate, Frame, PageTemplate, Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from SdObject import *   
from SdMessage import * 
from SdParser import * 

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']

# bodytext  style used for wrapping  data on flowables 
styles = getSampleStyleSheet()
#styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER


sdName = Paragraph('''<b>LTE-IMSI based Attach</b>''', styleBH)
moduleA = Paragraph('''<b>RAN</b>''',  styleBH)
moduleB = Paragraph('''<b>CN</b>''', styleBH)

componentA = Paragraph('''<b>UE</b>''',  styleBH)
componentB = Paragraph('''<b>eNB</b>''', styleBH)
componentC = Paragraph('''<b>MME</b>''', styleBH)

produceBy = Paragraph('''<b>xLab Product</b>''', styleBH)
produceTime = Paragraph('''<b>2015.06.11</b>''', styleBH)


descrpcion = Paragraph('long long long long long long long long long long long long long long long long long long long long line ', styleN)
partida = Paragraph('1', styleN)


data= [[sdName],
       [moduleA, '', moduleB, produceBy],
       [componentA, componentB, componentC, produceTime]]

table = Table(data)

table.setStyle(TableStyle([
                       ('BOX', (0,0), (-1,2), 0.25, colors.black),
                       #('BOX', (0,1), (-1,2), 0.25, colors.black),                       
                       ('ALIGNMENT', (0,0), (-1,2), 'CENTER'),
                       ('GRID', (0,1), (-1,-1), 0.25, colors.black),
                       ]))


def myTitlePage(canvas, doc):
    pass

def header(canvas, doc):
    canvas.saveState()
    P = Paragraph("This is a multi-line footer. It goes on every page. " * 5, styleN)
    w, h = P.wrap(doc.width, doc.topMargin)
    #P.drawOn(canvas, doc.leftMargin, 730)

    table.wrapOn(canvas, 500, 300)
    table.drawOn(canvas, doc.leftMargin, 730)

    fParser = SdParser("demo.txt")
    fParser.load()

    objList = fParser.objList

    for i in range(len(objList)):
        print objList[i], i
        obj = SdObject(objList[i], i+1)
        obj.draw(canvas)

    #canvas.showPage()                      
    #canvas.save()

    msgList = fParser.msgList

    itemStart = 4 * (doc.page-1) + 1
    itemEnd = 5 * (doc.page-1) -1

    if (itemStart >= msgList):
        itemStart = 0
        itemEnd = 0
    elif (itemEnd >= msgList):
        itemEnd = len(msgList)

    print "BBC:", len(msgList), doc.page, itemStart, itemEnd

    if (doc.page == 2) :
        for i in range(0, 3):
            #print msgList[i], i
            print msgList[i][0], msgList[i][1], msgList[i][2]
            senderInx = objList.index(msgList[i][0])
            receiverInx = objList.index(msgList[i][1])   
            print senderInx, receiverInx
            obj = SdMessage(msgList[i][2], senderInx+1, receiverInx+1, i+1, msgList[i][3])
            obj.draw(canvas)
    elif (doc.page == 3):
        for i in range(4, 6):
            #print msgList[i], i
            print msgList[i][0], msgList[i][1], msgList[i][2]
            senderInx = objList.index(msgList[i][0])
            receiverInx = objList.index(msgList[i][1])   
            print senderInx, receiverInx
            obj = SdMessage(msgList[i][2], senderInx+1, receiverInx+1, i+1, msgList[i][3])
            obj.draw(canvas)

    canvas.restoreState()

doc = SimpleDocTemplate('demo.pdf', pagesize=letter)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
template = PageTemplate(id='test', frames=frame)
doc.addPageTemplates([template])

text = []
for i in range(210):
    text.append(Paragraph("This is a multiline %d tests." % i, styleN))

doc.build(text, onFirstPage=myTitlePage, onLaterPages=header)