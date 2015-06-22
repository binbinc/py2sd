
import re
from SdObject import *   
from SdMessage import * 

class SdParser:

    def __init__(self, fileName):
        self.objList = []
        self.msgList = []       

    def transEachLine(self, line):
        #components: a, b, c
        comps = re.compile("^components:\s*(\w)[,\s*(\w)]*")
        matchComp = comps.search(line)
        if matchComp:
            tempObjList1 = matchComp.group().strip("components:").strip("\n")
            tempObjList2 = tempObjList1.split(',')
            for i in range(len(tempObjList2)):
                self.objList.append(tempObjList2[i].strip(" "))
            print self.objList

        #"Message" : a -> b  (* A simple message exchange *)
        item1 = re.compile(r"^\"\w+[\s*\w*]*\"")
        matchMsg1 = item1.search(line)
        tempList = ""
        if matchMsg1:
            tempList = matchMsg1.group().strip("\"")
            print "Msg is: ", tempList

        item2 = re.compile(r"\(\w+[,\s*\w*]*\)")
        matchMsg2 = item2.search(line)
        #if matchMsg2:
            #print "MessageNote: ", matchMsg2.group().strip("(").strip(")")

        item4 = re.compile(r"\(\*\s+.*\*\)") 
        matchMsg4 = item4.search(line)
        msgDetail = []
        if matchMsg4:
            msgDetail = matchMsg4.group().strip("(*").strip("*)")

        item3 = re.compile(r"\s*(\w+)\s*(->|=>|<-|<=|<->)\s*(\w+)")
        matchMsg3 = item3.search(line)
        if matchMsg3:
            tempList3 = matchMsg3.groups()
            print "MessageSequence: ", tempList3

            if (len(tempList3) == 3):
                a = tempList3[0]
                b = tempList3[2]

                if (cmp(tempList3[1], '->') == 0):
                    print ''
                    self.msgList.append((a,b,tempList, msgDetail))
                else:
                    self.msgList.append((b,a,tempList, msgDetail))
            print self.msgList
        
        #print matchMsg1, matchMsg2, matchMsg3, matchMsg4

    def load(self):
        f = open("demo.txt", "r")
        while True:  
            line = f.readline()  
            if line:  
                self.transEachLine(line)   
            else:  
                break
        f.close()             
 
