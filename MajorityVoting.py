import codecs

def readlabels(lblseries,startindex,endindex):
    dictLabel={}
    for index in range(startindex,endindex+1):#endindex+1 becuse range(0,2) is:0,1
        flabel=codecs.open(lblseries+str(index),"r",encoding='utf-8')
        i=0
        for lbl in flabel:
            lst=[]
            if i in dictLabel:
                lst=dictLabel[i]
            lst.append(lbl)
            dictLabel[i]=lst
            i+=1
        #end for------------------
        flabel.close()
    #end for----------------------
    return dictLabel

def readlabels(lblseries,lstindex):
    dictLabel={}
    for index in lstindex:#endindex+1 becuse range(0,2) is:0,1
        flabel=codecs.open(lblseries+str(index),"r",encoding='utf-8')
        i=0
        for lbl in flabel:
            lst=[]
            if i in dictLabel:
                lst=dictLabel[i]
            lst.append(lbl)
            dictLabel[i]=lst
            i+=1
        #end for------------------
        flabel.close()
    #end for----------------------
    return dictLabel

def splitLabelCount(lstRow):
    dictLabelCount={}
    for lbl in lstRow:
        if lbl in dictLabelCount:
            dictLabelCount[lbl]=int(dictLabelCount[lbl])+1
        else:
            dictLabelCount[lbl]=1
    return dictLabelCount

def majorityVoting(dictLabelCount):
    maxKey="none"
    maxVal=0
    for key in dictLabelCount:
        val=int(dictLabelCount[key])
        if val>maxVal:
            maxVal=val
            maxKey=key
            
    if maxKey=="none":
         raise Exception("error can not find label:" % maxKey)
    return maxKey

def writelabels(dictFinal,outFileName):
    fout=codecs.open(outFileName,"w",encoding='utf-8')
    for key in dictFinal:
        strOut=dictFinal[key]
        fout.write(strOut)
    fout.close()

def voitng(dictLabel):
    dictFinal={}
    i=0
    for key in dictLabel:
        dictLabelCount={}
        lst=[]
        lst=(dictLabel[key])#OUTPUT EXAMPLE:[O,O,I]
        dictLabelCount=splitLabelCount(lst)#OUTPUT EXAMPLE:dictLabelCount={O:2,I:1}
        votLabl=majorityVoting(dictLabelCount)
        dictFinal[i]=votLabl#OUTPUT EXAMPLE:O
        i+=1
    return dictFinal
#end For--------------------
##################################<<<main code>>>####################################
if __name__=='__main__':
    lblseries=input("enter label series:")
    startindex=input("first of index of label is:")
    endindex=input("last index of labels is:")
    startindex=int(startindex)
    endindex=int(endindex)

    dictLabel={}
    dictLabel=readlabels(lblseries,startindex,endindex)#OUTPUT EXAMPLE:dictLabel={0:[O,O,I],1:[O,B,O],2:[B,B,I]}

    print("start voting...")

    dictFinal={}
    dictFinal=voitng(dictLabel)

    writelabels(dictFinal,'votinglabel')
    print("complated!!!!")
