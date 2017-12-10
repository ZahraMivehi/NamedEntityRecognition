import codecs

def spamSentence(lblList,skipLabel):
    for lbl in lblList:
        if lbl!=skipLabel:
            return False
    return True

namefin = input("enter Teain file name:")
skipLabel=input("enter label for skip:")
fin=codecs.open(namefin,"r", encoding='utf-8')#open as utf
fout=codecs.open("Clean_"+namefin,"w",encoding='utf-8')
lblList=[]
lstLine=[]
for row in fin :
    lstLine.append(row)
    line=row.strip()
    if line !="":
        lstTokens=[]
        lstTokens=line.split(" ")
        if lstTokens[0]!=".":
            lbl=lstTokens[1].strip()
            lblList.append(lbl)
        else:
            if not(spamSentence(lblList,skipLabel)):
                strOut=''.join(map(str, lstLine))
                strOut=strOut#+"\n"
                fout.write(strOut)
            lblList=[]
            lstLine=[]
fin.close()
fout.close()
