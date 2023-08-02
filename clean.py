from nltk.stem import PorterStemmer

def clean(filenom): 
     list=[]
     with open (filenom+".txt", "r") as f1:
          for line in f1:
               for word in line.split():
                    list.append(word)
     ps=PorterStemmer()
     list2=[]
     for word in list:
          list2.append(ps.stem(word)+" ")
     
     with open(filenom+".txt","w") as f1:
          f1.writelines(list2)

