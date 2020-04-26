# -*- coding: utf-8 -*-


import pandas as pd

df = pd.read_csv ('CSV file', encoding = "ISO-8859-1")
#print (df.head(10))



#To replace ','
df = df.replace(',','', regex=True)

#To replace $ sign
df['Total_Gross'] = df['Total_Gross'].replace({'\$':''}, regex = True)

#To replace empty rows with 0
df["Total_Gross"] = df["Total_Gross"].fillna(0)

#To replace empty rows with 0
df["Distributor"] = df["Distributor"].fillna('Indipendent')

#To convert the column type to int
df["Total_Gross"] = df["Total_Gross"].astype(str).astype(int)

#Calculate stats
mean1 = df['Total_Gross'].mean()
sum1 = df['Total_Gross'].sum()
max1 = df['Total_Gross'].max()
min1 = df['Total_Gross'].min()
count1 = df['Total_Gross'].count()
median1 = df['Total_Gross'].median() 
std1 = df['Total_Gross'].std() 
var1 = df['Total_Gross'].var()  

#Group distributors by sum and count
groupby_sum1 = df.groupby(['Distributor']).sum() 
groupby_count1 = df.groupby(['Distributor']).count()

#Print the stats
print ('Mean Total Gross: ' + str(mean1))
print ('Sum of Total Gross: ' + str(sum1))
print ('Max Total Gross: ' + str(max1))
print ('Min Total Gross: ' + str(min1))
print ('Count of Total Gross: ' + str(count1))
print ('Median Total Gross: ' + str(median1))
print ('Std of Total Gross: ' + str(std1))
print ('Var of Total Gross: ' + str(var1))

#Print the distributors
print ('Sum of values, grouped by the Distributor: ' + str(groupby_sum1))
print ('Count of values, grouped by the Distributor: ' + str(groupby_count1))

#To plot the distributors with most number of movies using bar plot
df['Distributor'].value_counts()[:10].plot(kind='barh')



