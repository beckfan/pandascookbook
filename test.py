# coding=UTF-8
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',20)  # a就是你要设置显示的最大列数参数
pd.set_option('display.max_rows',50)  # b就是你要设置显示的最大的行数参数
pd.set_option('display.width',1000)  # x就是你要设置的显示的宽度，防止轻易换行
dfvisit=pd.read_excel('I:/pandasdata/visitlist.xlsx')
dfvisit=dfvisit.dropna(subset=['Category'])
print dfvisit.isnull().sum()
#print dfvisit.describe()
#print dfvisit.dtypes
#print type(dfvisit.Owner)
SrOwner=dfvisit.Owner
SrOwner.value_counts().plot()
#plt.show()
#print SrOwner.sizeoooooooo

SrPotential=dfvisit['Sales Potential']
#print type(SrPotential)

#print SrPotential.count()
#print SrPotential.size
#SrPotential.fillna('To be defined',inplace=True)
#print SrPotential