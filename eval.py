import os
import random
import subprocess
import MajorityVoting
#from MajorityVoting import readlabels
def getIndexLabelFiles(lstLabel):
    lstTrue=[]
    i=0
    for index in lstLabel:
        if index==1:
            lstTrue.append(i)
        i+=1
    return lstTrue
def writeEval(lstLabelFiles,linestring):
    feval=open("finaleval.txt","w")
    strOut=' '.join(map(str, lstLabelFiles))
    strOut="Labels Group:"+strOut
    feval.write(strOut)
    feval.write("\n"+linestring)
    feval.close()
############################## MAIN ###########################
##dicFScores={}
##dicFScores['G1']=69.83
##dicFScores['G2']=62.04
##dicFScores['G3']=62.01
##dicFScores['G1,2']=69.22
##dicFScores['G2,3']=62.04
##dicFScores['G1,3']=69.37
##dicFScores['G1,2,3']=66.48

maxKey='G1'
maxFScore=69.83

lblseries=input("enter label series:")
firstIndex=input("enter first index:")
lastIndex=input("enter last index:")
lblRefFile=input("Enter Refrence Name:")
maxfscore=input("enter f-score mark:")
countRand=input("enter count of voting random:")
for i in range(int(countRand)):
    lst=[]
    for j in range(int(firstIndex),int(lastIndex)):
        lst.append(random.randint(0,1))
        
    lstFile=[]
    lstFile=getIndexLabelFiles(lst)#get file where value in lst is 1

    dictLabel={}
    dictLabel=MajorityVoting.readlabels(lblseries,lstFile)

    dictFinal={}
    dictFinal=MajorityVoting.voitng(dictLabel)
    MajorityVoting.writelabels(dictFinal,'voting')

    command="perl c:\\py\\evalIOB2.pl c:\\py\\"+lblRefFile+" c:\\py\\voting>c:\\py\\tempevaluation.txt"

    os.system(command)
    #os.system("start cmd.exe @cmd /k "+command)#if you want to view result in cmd use this for help
    fvot=open("tempevaluation.txt","r")
    for line in fvot:
        if 'FULLY CORRECT answer with class info' in line:
            lst=[]
            lst=line.split(" ")
            fscore=str(lst[16])
            fscore=fscore.replace(")","")
            fscore=fscore.replace(",","")
            if float(fscore)>float(maxfscore):
                maxfscore=fscore
                writeEval(lstFile,line)
                print(">>>>>>>>>>>>>>>new f-score:"+maxfscore)
            else:
                print("fscore:"+fscore)
    fvot.close()
print('Complated!...')
