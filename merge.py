import csv
import pandas as pd
file1="bright_stars.csv"
file2="unit_star.csv"

#list to store data from file
d1=[]
d2=[]

with open(file1,"r")as f:
    c=csv.reader(f)
    for i in c:
        d1.append(i)


with open(file2,"r") as f:
    c=csv.reader(f)
    for i in c:
        d2.append(i)


#headers of both files
h1=d1[0]
h2=d2[0]

pd1=d1[1:]
pd2=d2[1:]

#merge headers
h=h1+h2

#merging data
pd=[]
for i in pd1:
    pd.append(i)
for j in pd2:
    pd.append(j)
    
#lets create new file
with open('total_stars.csv',"w")as f:
    c=csv.writer(f)
    c.writerow(h)
    c.writerows(pd)