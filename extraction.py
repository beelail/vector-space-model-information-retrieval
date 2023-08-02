import os
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def extract(filename):
    listmotfile=[]
    special="(){}§!?%&*¨'""^£$#:;-_."
    with open (filename+".txt", "r") as f1:
        for line in f1:
            for word in line.split():
                for i in special:
                    word=word.replace(i,'')
                listmotfile.append(word+" ")   
    listmotclean=[word for word in listmotfile if word not in stopwords.words('french')]

    with open (filename+"clean.txt", "w") as f1:
        f1.writelines(listmotclean)