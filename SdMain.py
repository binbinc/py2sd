# -*- coding: utf-8 -*- 
#字体库
import reportlab.lib.fonts              
#canvas画图的类库
from reportlab.pdfgen.canvas import Canvas  
#用于定位的inch库，inch将作为我们的高度宽度的单位
from reportlab.lib.units import inch 

from SdObject import *   
from SdMessage import * 
from SdParser import * 

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

if __name__ == "__main__":

    fParser = SdParser("demo.txt")
    fParser.load()

    objList = fParser.objList

    can = Canvas('demo.pdf')  
    can.setFont("Helvetica-Bold", 11.5)  

    for i in range(len(objList)):
    	print objList[i], i
        obj = SdObject(objList[i], i+1)
        obj.draw(can)

    msgList = fParser.msgList

    for i in range(len(msgList)):
    	#print msgList[i], i
    	print msgList[i][0], msgList[i][1], msgList[i][2]
    	senderInx = objList.index(msgList[i][0])
     	receiverInx = objList.index(msgList[i][1])   
     	print senderInx, receiverInx
        obj = SdMessage(msgList[i][2], senderInx+1, receiverInx+1, i+1)
        obj.draw(can)

    #showpage将保留之前的操作内容之后新建一张空白页
    can.showPage()                      
    #将所有的页内容存到打开的pdf文件里面。
    can.save()   

    for i in range(len(msgList)):
    	#print msgList[i], i
    	print msgList[i][0], msgList[i][1], msgList[i][2]
    	senderInx = objList.index(msgList[i][0])
     	receiverInx = objList.index(msgList[i][1])   
     	print senderInx, receiverInx
        obj = SdMessage(msgList[i][2], senderInx+1, receiverInx+1, i+1)
        obj.draw(can)
    
    #showpage将保留之前的操作内容之后新建一张空白页
    can.showPage()                      
    #将所有的页内容存到打开的pdf文件里面。
    can.save()  

    text = []

    #doc.build(text)


