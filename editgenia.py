import codecs
#---------------------------------------------------------------------
def removeEmptyLine(namePos,outName):
    fPOS=codecs.open(namePos,"r", encoding='utf-8')
    fout=codecs.open(outName,"w",encoding='utf-8')
    flag=False
    for token in fPOS :
        if token !="\n":
            fout.write(token)
        elif token=="\n" and flag==False:
            flag=True
            continue
        elif token=="\n" and flag==True:
            fout.write(token)
        flag=False
    
    fPOS.close()
    fout.close()
#---------------------------------------------------------------------
def removeSpamLine(withoutEmptyName,outName):
    fPOS=codecs.open(withoutEmptyName,"r", encoding='utf-8')
    fout=codecs.open(outName,"w",encoding='utf-8')
    flag=True
    for token in fPOS :
        #print(token,flag)
        if flag==True:
            fout.write(token)
            flag=False
        else:
            flag=True
        #--------------
        if token=="\n" or token=="":
            #print("xxx")
            flag=True

    fPOS.close()
    fout.close()  
#---------------------------------------------------------------------
OUT_NAME_TEST="editedPOSTest"
OUT_NAME_TRAIN="editedPOSTrain"
OUT_NAME_TEMP_TRAIN="editedPOSTrainTemp"

namePos = input("What's genia postagger file name? ")
choose=input("1-test\n2-train\n")
print("please waite...")
if choose=="1":
    removeEmptyLine(namePos,OUT_NAME_TEST)
elif choose=="2":
    removeEmptyLine(namePos,OUT_NAME_TRAIN)
    #removeEmptyLine(namePos,OUT_NAME_TEMP_TRAIN)
    #removeSpamLine(OUT_NAME_TEMP_TRAIN,OUT_NAME_TRAIN)
print("complated!")
input("press enter to exit...")
