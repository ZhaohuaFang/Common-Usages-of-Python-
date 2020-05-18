#1. Extract Columns and Rows of an Excel

import xlrd

workbook=xlrd.open_workbook('filename')

#declare the sheet you want to open
sheet=workbook.sheets()[0]

#declare the column you want to obtain
column=sheet.col_values(1) 

#declare the row you want to obtain
row=sheet.row_values(1)

#2. Delete Specific Elements in a List with Index
del list[0]

#It should be noted that the 0th element has been deleted. 
#Once you use
del list[0]
#again, you will delete the 1th element of the original list.

#3. Separate Each Word in a Sentence
import re 
words=re.findall(r'\b\w+', sentence)

#for example,
words=re.findall(r'\b\w+', 'I love travel...')
print(words)
#['I', 'love', 'travel']

#4. Add, Subtract, Multiply and Divide Each Element in a List by the Same Number
import numpy as np
a=[1,1,2,2]
#convert list to array
a=np.array(a)
a+=1
a-=1
a=a*3
#convert array to list
a=list(a)
print(a)
#[3, 3, 6, 6]

#5. Extract the Year, Month and Day from a String
import dateutil.parser as parser
n=parser.parse('8/31/2015').month
print(n)
#8
n=parser.parse('2020/4/8').day
print(n)
#8

#6. Inverse a List
list=[1,2,3,4]
list=list[::-1]
print(list)
#[4, 3, 2, 1]

#so, what is
list[::-2]
list[::2]
list[2::]
list[2]

list=[1,2,3,4]
for i in list[::2]:
    print(i)
#1
#3

#7. Lots of Colors
import seaborn
plt.plot(x,y,c=seaborn.xkcd_rgb['red'])

#for more colors, you can visit
#https://blog.csdn.net/weixin_40683253/article/details/87370127.

#8. Generate Dates at Monthly Intervals
import pandas as pd
def sequence_of_months():
  a=pd.date_range('20020402', '20150831',freq='M')  
  
  return a
"""
DatetimeIndex(['2002-04-30', '2002-05-31', '2002-06-30', '2002-07-31',
               '2002-08-31', '2002-09-30', '2002-10-31', '2002-11-30',
               '2002-12-31', '2003-01-31',
               ...
               '2014-11-30', '2014-12-31', '2015-01-31', '2015-02-28',
               '2015-03-31', '2015-04-30', '2015-05-31', '2015-06-30',
               '2015-07-31', '2015-08-31'],
              dtype='datetime64[ns]', length=161, freq='M')
"""
#9. Generate Arithmetic Sequence
x=np.linspace(1,10,5)
#[ 1.    3.25  5.5   7.75 10.  ]

#10. Calculate the Related Coefficient
import pandas as pd
a=[1,2,3,1]
b=[2,4,6,9]
a = pd.Series(a) 
b = pd.Series(b)
 
corr_gust = round(a.corr(b), 4) 
print('corr_gust :', corr_gust)
#corr_gust : 0.0291

#11. Output non-static values When Plotting
plt.title('This is' + str(non-static value), fontsize=12) 

