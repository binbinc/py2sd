from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']

# bodytext  style used for wrapping  data on flowables 
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
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

produceBy = Paragraph('''<b>ZTE LTE Product</b>''', styleBH)
produceTime = Paragraph('''<b>2015.04.12</b>''', styleBH)


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

def header(canvas, doc):
    canvas.saveState()
    P = Paragraph("This is a multi-line footer. It goes on every page. " * 5, styleN)
    w, h = P.wrap(doc.width, doc.topMargin)
    #P.drawOn(canvas, doc.leftMargin, 730)

    table.wrapOn(canvas, 500, 300)
    table.drawOn(canvas, doc.leftMargin, 730)

    canvas.restoreState()

doc = BaseDocTemplate('test.pdf', pagesize=letter)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
template = PageTemplate(id='test', frames=frame, onPage=header)
doc.addPageTemplates([template])

text = []
for i in range(111):
    text.append(Paragraph("This is line %d." % i, styleN))
doc.build(text)