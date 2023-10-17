import pandas as pd
df=pd.read_excel(r'C:\Users\bharg\Downloads\sampledataworkorders\sampledataworkorders.xlsx',sheet_name='WOs',header=0)
print(df)
df.shape
print(len(df))  #prints the number of rows
print(df.count()) # gets the column wise nonnull values
print(df.columns)

print(df.head())
