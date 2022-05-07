import pandas as pd
df=pd.read_csv('dwarf_stars.csv')
print(df.columns)
print(df.dtypes)
df=df.dropna()
#converting radius
df["Radius"]= 0.102763*df["Radius"]
#converting mass object to float 
df["Mass"]= df["Mass"].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
print(df.dtypes)
df["Mass"]=0.000954588*df["Mass"]

print(df.head)
print(df.columns)
df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(df.columns)

#reset index because we have used dropna() to tremove nan values 
df.reset_index(drop=True,inplace=True)
 #creating new file for merging
df.to_csv("unit_star.csv")