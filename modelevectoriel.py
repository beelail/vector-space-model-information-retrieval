import clean 
import extraction
import math
import operator


def wordlist(filename):
    list=[]
    with open (filename+".txt", "r") as f1:
        for line in f1:
            for word in line.split():
                list.append(word)
    return list 

def nb(l):
    j=0
    for i in l:
        if i!=0:
            j+=1
    return j

def vectoriel(corpus):
    for i in corpus:
        extraction.extract(i)
        clean.clean(i+"clean")


    listcorpusmot=[] 
    for i in corpus :
        listcorpusmot.append(wordlist(i+"clean"))


    querywordlist=wordlist("queryclean")   

    tf={}
    for word in querywordlist:
        l=[]
        for i in listcorpusmot:
            l.append(i.count(word))
            tf[word]=l


    wij={}
    for word in querywordlist:
        l5=[]
        for j in tf[word]:
            l5.append(j*math.log10(len(corpus) /(1+math.log10(1+nb(tf[word])))))
        wij[word]=l5



    sim={}
    for j in range (0,len(corpus)):
        k=0
        l=0
        for i in querywordlist:
            k+=wij[i][j]
            l+=math.pow(wij[i][j],2)
        if (l!=0):
            sim[corpus[j]+".txt,query"]=k/math.sqrt(l*len(querywordlist))
        else:
            sim[corpus[j]+".txt,query"]=0

    sim=sorted(sim.items() ,key=operator.itemgetter(1), reverse=True)
    print(sim)


query=input("give query : ")
with open ("query.txt","w")as f1:
    f1.write(query)

extraction.extract("query")
clean.clean("queryclean")
corpus=["xml","reseau","bd"]
vectoriel(corpus)