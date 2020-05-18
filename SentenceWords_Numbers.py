import xlrd
import re 
import  tensorflow as tf
import  numpy as np
import pandas as pd
from    tensorflow import keras
workbook=xlrd.open_workbook('filename')
sheet=workbook.sheets()[0]

a=sheet.col_values(12) 


#create a list to store words
m=[]
for i in range(len(a)):
                                                   
        b1=re.findall(r'\b\w+', a[i])
        #Give all the words in all the sentences to m
        for j in b1:
            m.append(j)

d = {'col': m}
df = pd.DataFrame(data=d)
uniq_lab = np.unique(df['col'])

for lab in uniq_lab:
    df['col']= pd.factorize(df.col)[0]
#df matches words' position and words' number
#print(df)
df=np.array(df)
#print(df)


sentence=[]
time=0
for i in range(len(a)):
    b2=re.findall(r'\b\w+', a[i])
    
    l=[]
    for j in range(len(b2)):
        
        index=df[j]
        l.append(index)
    
    sentence.append(l)
    
    for k in range(len(b2)):
        df=np.delete(df,[0])
#delete the title
del sentence[0]


length=0
#get the biggest length of the sentences in sentence
for i in sentence:
    b=len(i)
    if b>length:
        length=b
print(length)
sentence=np.array(sentence)

x_train = keras.preprocessing.sequence.pad_sequences(sentence,maxlen=23)  
db_train = tf.data.Dataset.from_tensor_slices(x_train).batch(10)
sample=next(iter(db_train))
print(sample)
