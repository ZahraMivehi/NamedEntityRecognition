import codecs
import random
#---------------------- Case feature---------------
def isCapital(token):
 if token !="":
  if token.isupper()==False and isMixed(token)==False:
   char=token[0]
   return char.isupper()
 return False
#----------------------------------------------------
def isMixed(token):
 if token !="":
  if token.isupper()==False:
   t1=token[1:]
   for c in t1:
    if c.isupper():
     return True
 return False
#---------------------- orthographic feature--------
def isEndCap(token):
    if token !="":
        l=token[-1:]#get last char
        if l.isupper():
            return True
    return False

#-----------------------------------------------------------------
def isSymbols(token):
    if token !="":
        lstS=["-","/","(",")","[","]",":",";",\
              ",",".","ves","'","\"","%","*","=","+"]

        for c in token:
            if c in lstS:
                return True
    return False
#---------------------- digit feature---------------
def isfloat(token):
 if token.isnumeric()==False:
  try:
   float(token)
   return True
  except ValueError:
   return False
 return False
#----------------------------------------------------
def wordWhitNumber(token):
 if not(token.isnumeric()) and not(isfloat(token)):
  return any(char.isdigit() for char in token)
 return False
#----------------------------------------------------
def romanNumeral(token):
 if token !="":
   token = token.upper()
   validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I"]
   for letters in token:
    if letters not in validRomanNumerals:
     return False
   return True
 return False
#----------------------Ponectutation--------------------
def endsWithPeriod(token):
 if token !="":
  lstp=[".", "," , "?" , "!" , "-" , ")" , "]" , "&","\""]
  ln=len(token)
  ch=token[ln-1]
  if ch in lstp:
   return True
 return False
#----------------------Character------------------------
def isPossessive(token):
 if token !="":
  lstch=["i" , "you", "we", "he" , "she", "they" , "it" , "me" ,\
         "him","her" ,"us" , "them" , "my" , "mine","your","yours","our",\
         "ours","its","their","theirs"]
  token=token.lower()
  if token in lstch:
   return True
 return False
#----------------------------------------------------
def isGreek(token):
 if token !="":
  greek_alphabet = {
  u'\u0391': 'Alpha',
  u'\u0392': 'Beta',
  u'\u0393': 'Gamma',
  u'\u0394': 'Delta',
  u'\u0395': 'Epsilon',
  u'\u0396': 'Zeta',
  u'\u0397': 'Eta',
  u'\u0398': 'Theta',
  u'\u0399': 'Iota',
  u'\u039A': 'Kappa',
  u'\u039B': 'Lamda',
  u'\u039C': 'Mu',
  u'\u039D': 'Nu',
  u'\u039E': 'Xi',
  u'\u039F': 'Omicron',
  u'\u03A0': 'Pi',
  u'\u03A1': 'Rho',
  u'\u03A3': 'Sigma',
  u'\u03A4': 'Tau',
  u'\u03A5': 'Upsilon',
  u'\u03A6': 'Phi',
  u'\u03A7': 'Chi',
  u'\u03A8': 'Psi',
  u'\u03A9': 'Omega',
  u'\u03B1': 'alpha',
  u'\u03B2': 'beta',
  u'\u03B3': 'gamma',
  u'\u03B4': 'delta',
  u'\u03B5': 'epsilon',
  u'\u03B6': 'zeta',
  u'\u03B7': 'eta',
  u'\u03B8': 'theta',
  u'\u03B9': 'iota',
  u'\u03BA': 'kappa',
  u'\u03BB': 'lamda',
  u'\u03BC': 'mu',
  u'\u03BD': 'nu',
  u'\u03BE': 'xi',
  u'\u03BF': 'omicron',
  u'\u03C0': 'pi',
  u'\u03C1': 'rho',
  u'\u03C3': 'sigma',
  u'\u03C4': 'tau',
  u'\u03C5': 'upsilon',
  u'\u03C6': 'phi',
  u'\u03C7': 'chi',
  u'\u03C8': 'psi',
  u'\u03C9': 'omega',
  }
  for c in token:
      if c in greek_alphabet:
          return True
 return False
#----------------------Morphology------------------------
def isSuffix(token):
    if token !="":
        #https://www.learnthat.org/pages/view/suffix.html
        lsts=["able","ac","acity","ocity","ade","age","aholic","oholic",\
          "al","algia","an","ance","ant","ar","ard","arian","arium", \
          "orium","ary","ate","ation","ative","cide","cracy","crat",\
          "cule","cy","cycle","dom","dox","ectomy","ed","ee","eer","emia", \
          "en","ence","ency","ent","er","ern","escence","ese","esque","ess",\
          "est","etic","ette","ful","fy","gam","gamy","gon","gonic",\
          "hood","ial","ian","iasis","iatric","ible","ic","ical","ile",\
          "ily","ine","ing","ion","ious","ish","ism","ist","ite","itis"\
          "ity","ive","ization","ize","less","let","like","ling","loger",\
          "logist","log","ly","ment","ness","oid","ology","oma","onym","opia"\
          "opsy","or","ory","osis","ostomy","otomy","ous","path","pathy",\
          "phile","phobia","phone","phyte","plegia","plegic","pnea","scopy",\
          "scope","scribe","script","sect","ship","sion","some","sophy",\
          "sophic","th","tion","tome","tomy","trophy","tude","ty",\
          "ular","uous","ure","ward","ware","wise","y"]
        for suffix in lsts:
            if token.endswith(suffix):
                return True
    return False 
#-----------------------------------------------------------------
def isPrefix(token):
    if token !="":
        lstp=["a","an","ab","ad","ac","as","ante","anti","auto","ben","bi",\
              "circum","co","com","con","contra","counter","de","di","dis",\
              "eu","ex","exo","ecto","extra","extro","fore","hemi","hyper",\
              "hypo","il","im","in","ir","inter","intra","macro","mal","micro",\
              "mis","mono","multi","non","ob","o","oc","op","omni","peri","poly",\
              "post","pre","pro","quad","re","semi","sub","super","supra",\
              "sym","syn","trans","tri","ultra","un","uni"]
        for Prefix in lstp:
            if token.startswith(Prefix):
                return True
    return False
#-----------------------------------------------------------------
def isCommonEnding(token):
    if token !="":
        lstc=["a","ae","ces","des","e","en","es","ges",\
              "i","ies","ves"]

        for commonEnding in lstc:
            if token.endswith(commonEnding):
                return True
    return False
#----------------------Lenght------------------------
def getLenght(token):
    if token!="":
        return len(token)
    return 0
#----------------------n-gram-------------------------
def set_n_gramNull(token,level):
    i=1
    count=0
    while(i<=level):
        if len(token)<i:
            count=count+1
        i=i+1
    return count
#------------------------------------
def n_gramPrefix(token,level):
    if token!="":
        if len(token)>=level:
            return token[:level]
        else:
            countNull=set_n_gramNull(token,level)
            str1=token+NULL_CHAR*countNull
            return str1
    return NULL_CHAR*level
#------------------------------------
def n_gramSuffix(token,level):
    if token!="":
        if len(token)>=level:
            return token[-level:]
        else:
            countNull=set_n_gramNull(token,level)
            str1=(NULL_CHAR*countNull)+token
            return str1
    return NULL_CHAR*level
#----------------------word shap------------------
def wordShap(token):
    #if index<0 or index>lst.count
    #token=lst[index]
    A=0
    a=0
    d=0
    z=0
    if token=="":
        return "z1"
    ws=""
    for c in token:
        if c.isupper():
            A+=1
        elif c.islower():
            a+=1
        elif c.isnumeric():
            d+=1
        else:
            z+=1
    if A>0:
        ws=ws+"A"+str(A)
    if a>0:
        ws=ws+"a"+str(a)
    if d>0:
        ws=ws+"d"+str(d)
    if z>0:
        ws=ws+"z"+str(z)
    return ws
#-----------------------------------------------
def wordShapByIndex(dictP,currentIndex,moveIndex):
    index=currentIndex+moveIndex
    tokenState=tokenInCurrentSentense(dictP,currentIndex,moveIndex)
    if not(tokenState):
        return NULL_CHAR
    else:
        lstP=[]
        lstP=dictP[index]
        if lstP[0]=="" or lstP[0]==" " or lstP[0]=="\n":
            return NULL_CHAR
        else:
            tokenP=lstP[0]
            return wordShap(tokenP)
    #else:
        #return "null"*abs(moveIndex)
        #return NULL_CHAR
#----------------------POS------------------------
def isPOS(token,tagLine,tag):
    if token !="":
        postok=tagLine.split("	")
        lst=[]
        lst=postok
        #print(lst)
        lst[0]=lst[0].strip()
        token=token.strip()
        #print(len(lst[0]),len(token))
        if token!=lst[0]:
            raise Exception("error(mismatch token):token=%s But postoken=%s" % (token,lst[0]))
        #print(lst)
        #try:
        if tag==lst[2]:
            return True
        #except Exception as error:
            #print(lst)
            #raise Exception("error(mismatch token):token=%s But postoken=%s " % (token,lst[0]))
    return False

#def getPOS(token,lstLine):
#    pos="null"
#    lstLine=dictPOS[i]
#    if token!=lstLine[0]:
#        raise Exception("error(mismatch token):token=%s But postoken=%s" % (token,lst[0]))
#    else:
#        pos=lstLine[2]
#    return pos
def tokenInCurrentSentense(dictP,currentIndex,moveIndex):
    index=currentIndex+moveIndex
    if not(index in dictP):
        return False
    else:
        if index>currentIndex:
            lst=range(currentIndex,index)
        elif index<currentIndex:
            lst=range(index,currentIndex)
        elif index==currentIndex:
            return True
    lstP=[]
    for i in lst:
        lstP=dictP[i]
        if lstP[0]=="" or lstP[0]==" " or lstP[0]=="\n":
            return False
    return True
#-----------------------------------------------------------                  
def getPOSByIndex(dictP,currentIndex,moveIndex):
    index=currentIndex+moveIndex
    tokenState=tokenInCurrentSentense(dictP,currentIndex,moveIndex)
    if not(tokenState):
        return NULL_CHAR
    else:
        lstP=[]
        lstP=dictP[index]
        if lstP[0]=="" or lstP[0]==" " or lstP[0]=="\n":
            return NULL_CHAR
        else:
            tokenP=lstP[2].strip()
            return tokenP
    #else:
        #return "null"*abs(moveIndex)
        #return NULL_CHAR
#----------------------------Base Form--------------------
def getBaseform(dictP,currentIndex,moveIndex):
    index=currentIndex+moveIndex
    tokenState=tokenInCurrentSentense(dictP,currentIndex,moveIndex)
    if not(tokenState):
        return NULL_CHAR
    else:
        lstP=[]
        lstP=dictP[index]
        if lstP[0]=="" or lstP[0]==" " or lstP[0]=="\n":
            return NULL_CHAR
        else:
            tokenP=lstP[1]
            return tokenP
    #else:
        #return "null"*abs(moveIndex)
        #return NULL_CHAR
#--------------------------------------------------------
def skipOutLabelsSentence(lblList,skipLabel):
    for lbl in lblList:
        if lbl!=skipLabel:
            return False
    return True
def removeSentenceOutLabel(dictSentence,lstIdOutSentence):
    c=0
    for idl in lstIdOutSentence:
        del dictSentence[idl]
        c+=1
    return c
def sortDictKeyByDigit(dictSentence):
    olddict={}
    olddict=dict(dictSentence)
    dictSentence={}
    #lend=len(dictSentence)
    j=0
    lstValues=olddict.values()
    for v in olddict.values():
        #print(k)
        dictSentence[j] =v
        j+=1
    return dictSentence
def createFileFromDictionery(dictSentence,fileName,countSentence):
    fRandout=codecs.open(fileName+"00","w",encoding='utf-8')
    t=0
    for t in range(countSentence):
        fRandout.write(dictSentence[t])
        fRandout.write("\n")
    fRandout.close()
def craeteRandomFiles(dictSentence,fileName,countFile,countSentence):
    for i in range(int(countFile)):
        fRandout=codecs.open(fileName+str(i),"w",encoding='utf-8')
        t=0
        for t in range(countSentence):
            rand=random.randint(0,countSentence)
            fRandout.write(dictSentence[rand])
            fRandout.write("\n")
        fRandout.close()

#--------------------------------------------------------
def getLabelLine(strLine):
    lstToken=[]
    lstToken=strLine.split(" ")
    ln=len(lstToken)
    lbl=lstToken[ln-1]
    return lbl

def createLabelTest(strSentense,fRefout):
    lstfin=strSentense.split("\n")
    for line in lstfin:
        lbl=getLabelLine(line)
        fRefout.write(lbl+"\n")

def removeLebelOfSentense(Sentense):
    lstLine=Sentense.split("\n")
    newSentense=""
    for line in lstLine:
        lstToken=line.split(" ")
        ln=len(lstToken)
        del lstToken[ln-1]
        newSentense=newSentense+' '.join(map(str, lstToken))+"\n"
    return newSentense
#--------------------------------------------------------
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()
#######################  Main  #####################
NULL_CHAR="^"
#fudict={"capitalCase":0,"upperCase":0,"mixed":0}
namefin = input("enter tokenized file:")
namefout=namefin+"Feature"
print("1-Test\n2-Train")
choose=input("Select Menue:")

if choose=="1":
    namePOS="editedPOSTest"
    numDiv=input("enter count of random partition:")#taqsim file test be chand qesmat mosavi ba jomalat tasadofi
elif choose=="2":
    namePOS="editedPOSTrain"
    numTrain=input("enter count of random Train:")
    removeOut=input("do you want to remove out of sentence label?[Y/N]:")

fin=codecs.open(namefin,"r", encoding='utf-8')#open as utf such as:greek char
fout=codecs.open(namefout,"w",encoding='utf-8')
fPOS=codecs.open(namePOS,"r", encoding='utf-8')
#------------------Load POS File----------------------
i=0

dictPOS={}
print(namePOS+" loading...")
for line in fPOS:
    dictPOS[i]=line.split("	")
    i+=1
    
fPOS.close()
#--------------------Proggress Bar--------------------
intP=i-1
#stepP=0
printProgressBar(0, i, prefix = 'Progress:', suffix = 'Complete', length = 50)
#if i >=100:
#    stepP=i//100
    
#-----------------------------------------------------
i=0
cs=0
sentence=""
lstlbl=[]
lstIdOutSentence=[]
dictSentence={}
for token in fin :
 strToken=token.strip() #remove hiden char such as enter key (\n)
 lstfin=[]
 lstfin=strToken.split(" ")
 strToken=lstfin[0].strip()
 flist=[]
 flist.append(strToken)
#------------------case features------------------
 if strToken!="": 
    flist.append(int(isCapital(strToken)))
    flist.append(int(strToken.isupper()))
    flist.append(int(isMixed(strToken)))
#---------------------- orthographic feature--------
    flist.append(int(isEndCap(strToken)))
    flist.append(int(strToken.islower()))
    flist.append(int(isSymbols(strToken)))
#------------------Digit features------------------
 
    flist.append(int(strToken.isnumeric()))
    flist.append(int(isfloat(strToken)))
    flist.append(int(wordWhitNumber(strToken)))
    flist.append(int(romanNumeral(strToken)))

#------------------Ponectutation features------------------
    flist.append(int(endsWithPeriod(strToken)))

#------------------Character features------------------
    flist.append(int(isPossessive(strToken)))
    flist.append(int(isGreek(strToken)))
#------------------Morphology features------------------
    flist.append(int(isSuffix(strToken)))
    flist.append(int(isPrefix(strToken)))
    flist.append(int(isCommonEnding(strToken)))
#------------------Length features------------------
    flist.append(int(getLenght(strToken)))
#------------------n-gram------------------------
    flist.append(n_gramPrefix(strToken,1))
    flist.append(n_gramPrefix(strToken,2))
    flist.append(n_gramPrefix(strToken,3))
    flist.append(n_gramPrefix(strToken,4))

    flist.append(n_gramSuffix(strToken,1))
    flist.append(n_gramSuffix(strToken,2))
    flist.append(n_gramSuffix(strToken,3))
    flist.append(n_gramSuffix(strToken,4))
#------------------word Shap------------------------
    flist.append(wordShapByIndex(dictPOS,i,-4))
    flist.append(wordShapByIndex(dictPOS,i,-3))
    flist.append(wordShapByIndex(dictPOS,i,-2))
    flist.append(wordShapByIndex(dictPOS,i,-1))

    flist.append(wordShap(strToken))

    flist.append(wordShapByIndex(dictPOS,i,+1))
    flist.append(wordShapByIndex(dictPOS,i,+2))
    flist.append(wordShapByIndex(dictPOS,i,+3))
    flist.append(wordShapByIndex(dictPOS,i,+4))
#------------------POS features------------------
##    flist.append(getPOSByIndex(dictPOS,i,-4))
##    flist.append(getPOSByIndex(dictPOS,i,-3))
##    flist.append(getPOSByIndex(dictPOS,i,-2))
##    flist.append(getPOSByIndex(dictPOS,i,-1))

##    flist.append(getPOSByIndex(dictPOS,i,0))

##    flist.append(getPOSByIndex(dictPOS,i,+1))
##    flist.append(getPOSByIndex(dictPOS,i,+2))
##    flist.append(getPOSByIndex(dictPOS,i,+3))
##    flist.append(getPOSByIndex(dictPOS,i,+4))
#----------------Baseform feature---------------
##    flist.append(getBaseform(dictPOS,i,-4))
##    flist.append(getBaseform(dictPOS,i,-3))
##    flist.append(getBaseform(dictPOS,i,-2))
##    flist.append(getBaseform(dictPOS,i,-1))
##
##    flist.append(getBaseform(dictPOS,i,0))
##
##    flist.append(getBaseform(dictPOS,i,+1))
##    flist.append(getBaseform(dictPOS,i,+2))
##    flist.append(getBaseform(dictPOS,i,+3))
##    flist.append(getBaseform(dictPOS,i,+4))
#----------------------------------------------
 if choose=="2" and strToken!="":#ver 960720
     flist.append(lstfin[1])#append lebel for Train,Test feauture dont have a label

 strOut=' '.join(map(str, flist))
 strOut=strOut+"\n"
     
 #print(strOut)
 fout.write(strOut)
#--------------------------------------------
 if strToken=="":#make a dictionery only for Train,to use make other random train file
     dictSentence[cs]=sentence
     sentence=""
     if choose=="2":
         if skipOutLabelsSentence(lstlbl,"O"):   
             lstIdOutSentence.append(cs)#save sentense number id ,that all label is O
         lstlbl=[]
     cs+=1
 elif strToken!="":
     if choose=="1":# make dic test(token+feautures+label) for split test whit refrence labels filse
         flist.append(lstfin[1])#append lebel
         strOut=' '.join(map(str, flist))
         strOut=strOut+"\n"
     sentence=sentence+strOut
     if choose=="2":
         lstlbl.append(lstfin[1])
     
#--------------------------------------------
 i+=1
 
 
 printProgressBar(i,intP,prefix = 'Progress:', suffix = 'Complete', length = 50)#just use in cmd(command Line)
 
fin.close()
fout.close()

cs-=1
if choose=="2":
    print("\nWaiting....start to make randdom Train...")
    i=0
    if removeOut=="Y":
        cs-=removeSentenceOutLabel(dictSentence,lstIdOutSentence)
        dictSentence=sortDictKeyByDigit(dictSentence)
    createFileFromDictionery(dictSentence,namefout,cs)
    craeteRandomFiles(dictSentence,namefout,numTrain,cs)
elif choose=="1":
    countSentense= cs // int(numDiv)
    print("\nnumDiv:",numDiv)
    print("\ncountSentense:",cs)
    print("\ncs//numDiv:",countSentense)
    i=0
    for i in range(int(numDiv)):
        fRandout=codecs.open(namefout+"Split"+str(i),"w",encoding='utf-8')
        fRefout=codecs.open(namefout+"Ref"+str(i),"w",encoding='utf-8')
        t=0
        for t in range(countSentense):
            rand=random.randint(0,countSentense)
            sentense=removeLebelOfSentense(dictSentence[rand])
            fRandout.write(sentense)
            #fRandout.write("\n")
            createLabelTest(dictSentence[rand],fRefout)
        fRandout.close()
        fRefout.close()
print("Complated!")
input("press enter to exit!")

    
    
        
